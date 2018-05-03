import datetime
import json
import ast
import operator

from functools import reduce

from django.db.models import Q
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt

from contacts.forms import ContactRequestCreate
from contacts.models import ContactRequest, DownloadDocumentUserRequest
from company.models import Admin, ContactUser
from company.tasks import send_email_to_admins
from elastic_pages.snippets import get_all_model_field_names
from products.models import Product, BespokeOrder, Touch, Technology, Spec
from products.snippets import serialize_sort_data


@csrf_exempt
def ajax_product_filter(request):
    data = ast.literal_eval(request.POST.get('data'))
    sort_params, touch, q = serialize_sort_data(data)
    context = {}
    context['filter_href'] = ''
    if touch == 'True':
        queryset = Product.objects.filter(
            **{
                'category__country_flag__abbreviation': request.country,
                'touch__isnull': False
            })
    elif touch == 'False':
        queryset = Product.objects.filter(
            **{
                'category__country_flag__abbreviation': request.country,
                'touch__isnull': True
            })
    else:
        queryset = Product.objects.filter(
            category__country_flag__abbreviation=request.country)

    # new_dict = {
    #     k: v for k, v in sort_params.items()
    #     if k in get_all_model_field_names(queryset.model)
    # }
    products = queryset.filter(
        reduce(operator.and_, (Q(name__contains=x) for x in q.split(' ')))
        ).filter(**sort_params)

    context['count'] = len(products)
    context['filter_href'] += 'page={}&'.format(1)
    for key, value in sort_params.items():
        context['filter_href'] += '{}={}&'.format(key, value)
    context['filter_href'] += 'touch={}&'.format(touch)
    return JsonResponse(context, safe=False)


@csrf_exempt
def ajax_product_key_filter(request):
    data = ast.literal_eval(request.POST.get('data'))
    context = {}
    if data:
        try:
            product = Product.objects.get(id=int(data))
            context['id'] = product.id
            context['category'] = product.category.id
            context['technology'] = product.category.technology.id
        except (ValueError, Product.DoesNotExist):
            keys = data.split(' ')
            products = Product.objects.filter(
                reduce(operator.and_, (Q(name__contains=x) for x in keys)))
            if products:
                context['products_keys'] = data
    return HttpResponse(json.dumps(context), content_type="application/json")


@csrf_exempt
def ajax_path_filter_sort(request):
    data = ast.literal_eval(request.POST.get('data'))
    sort_params, touch, q = serialize_sort_data(data)
    context = {}
    context['filter_href'] = ''
    for key, value in sort_params.items():
        context['filter_href'] += '{}={}&'.format(key, value)
    if touch == 'True':
        context['filter_href'] += 'touch=true&'
    elif touch == 'False':
        context['filter_href'] += 'touch=false&'
    if q:
        context['filter_href'] += 'q={}&'.format(q)
    context['filter_href'] = context['filter_href'][:-1]\
        .replace('category__technology__id', 'technology')
    return HttpResponse(json.dumps(context), content_type="application/json")


@csrf_exempt
def ajax_compare_product(request):
    context = {}
    data = ast.literal_eval(request.POST.get('data')).split(',')
    products = Product.objects.filter(id__in=data)
    context['products'] = []
    for product in products:
        data = product.get_info_list()
        data.update({
            'name': product.get_name(),
            'path': '/products/{}/{}/{}/'.format(
                product.category.technology.id,
                product.category.id, product.id),
        })
        if product.productimage_set.first():
            data.update({
                'image': product.productimage_set.first().image.url
            })
        context['products'].append(data)
    return JsonResponse(context, safe=False)


@csrf_exempt
def ajax_email_message_create(request):
    data = ast.literal_eval(request.POST.get('data'))
    form_data = {}
    for d in data:
        form_data.update({
            d.get('name', None): d.get('value', None)
        })
    form_data.pop('csrfmiddlewaretoken', None)
    form = ContactRequestCreate(form_data)
    form.head = 'Get In Touch/Email Us'
    form.to_email = ", ".join([admin.email for admin in Admin.objects.all()])
    if form.is_valid():
        form.save()
        email = ContactRequest.objects.last()
        user, created = ContactUser.objects.get_or_create(
            first_name=email.first_name,
            email=email.email,
            surname=email.surname,
            country=email.country,
            phone=email.phone,
            job=email.job_title
        )
        email.user = user
        email.head = 'Get In Touch/Email Us'
        email.to_email = ", ".join(
            [admin.email for admin in Admin.objects.all()])
        email.save()
        ctx = {
            'email': email,
        }
        message_txt = render_to_string('emails/get_in_touch_email.txt', ctx)
        send_email_to_admins.delay(form.head, message_txt, email.email)
        if request.is_ajax():
            return JsonResponse(form_data)
    else:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)


@csrf_exempt
def ajax_bespoke_order(request):
    if request.session.get('bespoke_order_created', False):
        item = BespokeOrder.objects.get(
            id=request.session['bespoke_order_created'])
        data = dict(ast.literal_eval(item.spec))
        serialized_data = get_serialized_dict_info(request.POST.dict(), data)
        data.update(serialized_data)
        item.spec = data
        item.save()
    else:
        serialized_data = get_serialized_dict_info(request.POST.dict(), False)
        date = datetime.datetime.now().date()
        item = BespokeOrder.objects.create(
            name='Bespoke Order, {}'.format(date.isoformat()),
            spec=serialized_data)
        request.session['bespoke_order_created'] = item.id
    return JsonResponse(item.spec, safe=False)


@csrf_exempt
def ajax_update_country(request):
    if not request.is_ajax() or not request.method == 'POST':
        return HttpResponseNotAllowed(['POST'])
    request.session['country'] = request.POST.get('country')
    return HttpResponse('ok')


@csrf_exempt
def ajax_download_docs(request):
    post_data = dict(request.POST)
    post_data.pop('csrfmiddlewaretoken', None)
    doc = post_data.pop('doc', None)
    data = {}
    for key, value in post_data.items():
        data[key] = value[0]
    user, status = DownloadDocumentUserRequest.objects.get_or_create(**data)
    if status:
        user.doc_title = doc[0]
        user.save()
    request.session['doc_download'] = True
    spec = Spec.objects.get(name=doc[0])
    return JsonResponse({'url': spec.file.url}, safe=False)


def get_serialized_dict_info(item, old):
    data = {}
    for key, value in item.items():
        key = key.title()
        if key == 'Technology':
            value = Technology.objects.get(id=value).name
        elif key == 'Dimension_W':
            if 'Dimension WxHxD (mm)' in old:
                values = old.get('Dimension WxHxD (mm)').split('x')
                value = ' {}x{}x{}'.format(value, values[1], values[2])
            else:
                value = '{} xx'.format(value)
            key = 'Dimension WxHxD (mm)'
        elif key == 'Dimension_H':
            if 'Dimension WxHxD (mm)' in old:
                values = old.get('Dimension WxHxD (mm)').split('x')
                value = '{}x {} x{}'.format(values[0], value, values[2])
            else:
                value = 'x {} x'.format(value)
            key = 'Dimension WxHxD (mm)'
        elif key == 'Dimension_D':
            if 'Dimension WxHxD (mm)' in old:
                values = old.get('Dimension WxHxD (mm)').split('x')
                value = '{}x{}x {}'.format(values[0], values[1], value)
            else:
                value = 'xx {}'.format(value)
            key = 'Dimension WxHxD (mm)'
        elif key == 'Size':
            key = 'Size (inches)'
        elif key == 'Touch':
            key = 'Touch Type'
            touch = Touch.objects.get(id=value)
            value = touch.type
            data['Touch Points'] = touch.points
        elif key == 'Brightness__Gte':
            key = 'Brightness (cd/m2)'
        elif key == 'Tft_Interface__Interface_Type':
            data['Interface'] = value
        data[key] = value
    return data
