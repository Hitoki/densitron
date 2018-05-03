import operator

from collections import OrderedDict
from itertools import chain
from functools import reduce

from django import template
from django.core.paginator import Paginator, EmptyPage
from django.core.urlresolvers import resolve
from django.db.models import Q
from django.shortcuts import get_object_or_404

from contacts.forms import ContactRequestCreate
from company.models import Address, Opportunity
from company.models import Team
from elastic_pages.models import VideoObject, GetInTouchBlock
from elastic_pages.snippets import calculate_paginate
from products.models import Product, Category, Technology, Service, \
    FAQ, Doc, TftIF, Touch, News, EvaluationKit, Twitt, SubService,\
    CountryFlag
from products.snippets import serialize_sort_data, get_news_map


register = template.Library()


@register.inclusion_tag('partials/header.html', takes_context=True)
def header_block(context, page_settings):
    return {
        'country': context.request.country,
        'logo': page_settings.header_block.logo_image.url,
        'auth_menu': page_settings.header_block.is_auth_menu,
        'soc_links': page_settings.header_block.soc_links.order_by(
            'priority'),
        'd_d_menu': page_settings.header_block.main_menus_elements.order_by(
            'priority')
    }


@register.inclusion_tag('partials/help_box_block.html')
def help_box_block(page_settings):
    return {
        'text': page_settings.help_box_block.text,
        'button': page_settings.help_box_block.button
    }


@register.inclusion_tag('partials/main_block.html', takes_context=True)
def main_block(context, page_settings):
    url = resolve(context.request.path_info)
    item = ''
    if url.url_name == 'services-service_detail':
        item = get_object_or_404(Service, id=context.get('service', 1))
    elif url.url_name == 'product-technology_detail':
        item = get_object_or_404(Technology, id=context.get('technology', 1))

    if item:
        text = item.description[:400] + '...'
        if item.short_description:
            text = item.short_description
        data = {
            'title': item.name,
            'text': text,
            'image': item.image.url
        }
    else:
        data = {
            'title': page_settings.main_block.title,
            'text': page_settings.main_block.text,
            'image': page_settings.main_block.background_image.url
        }
    return data


@register.inclusion_tag('partials/what_you_need_block.html',
                        takes_context=True)
def whatyouneed_block(context, page_settings):
    ctx = {
        'title': page_settings.what_you_need_block.title,
        'left_column_title':
            page_settings.what_you_need_block.left_column_title,
        'is_touch': page_settings.what_you_need_block.is_touch,
        'is_colour': page_settings.what_you_need_block.is_colour,
        'middle_column_title':
            page_settings.what_you_need_block.middle_column_title,
        'middle_column_label':
            page_settings.what_you_need_block.middle_column_label,
        'middle_column_caption':
            page_settings.what_you_need_block.middle_column_caption,
        'right_column_title':
            page_settings.what_you_need_block.right_column_title,
        'populars': Product.objects.filter(
            category__country_flag__abbreviation=
            context.get('request').country).order_by('-popularity')[:3],
    }
    return ctx


@register.inclusion_tag('partials/worldpay_box.html')
def worldpay_slide_block(page_settings):
    return {
        'slide_elems': page_settings.worldpay_slide_block.slide_elem.all(),
        'auto_slide': page_settings.worldpay_slide_block.auto_slide,
    }


@register.inclusion_tag('partials/posts_gallery_block.html')
def posts_gallery_block(page_settings):
    return {
        'title_left': page_settings.posts_gallery_block.title_left,
        'text_left': page_settings.posts_gallery_block.text_left,
        'image_left': page_settings.posts_gallery_block.image_left,
        'link_left': page_settings.posts_gallery_block.link_left or '',
        'title_middle': page_settings.posts_gallery_block.title_middle,
        'text_middle': page_settings.posts_gallery_block.text_middle,
        'image_middle': page_settings.posts_gallery_block.image_middle,
        'link_middle': page_settings.posts_gallery_block.link_middle or '',
        'title_right': page_settings.posts_gallery_block.title_right,
        'text_right': page_settings.posts_gallery_block.text_right,
        'image_right': page_settings.posts_gallery_block.image_right,
        'link_right': page_settings.posts_gallery_block.link_right or '',
    }


@register.inclusion_tag('partials/bespoke_screen_box.html')
def bespoke_screen_block(page_settings):
    return {
        'title_top': page_settings.bespoke_screen_block.title_top,
        'title_bottom': page_settings.bespoke_screen_block.title_bottom,
        'link': page_settings.bespoke_screen_block.link or '',
        'background': page_settings.bespoke_screen_block.background,
        'button': page_settings.bespoke_screen_block.button,
    }


@register.inclusion_tag('partials/latest_box.html')
def latest_block(page_settings):
    news = News.objects.all().order_by('-publicated')[:2]
    twitts = Twitt.objects.all().order_by('-publicated')[:2]

    return {
        'video_1': page_settings.latest_block.video_main,
        'video_2': page_settings.latest_block.video_second,
        'video_3': page_settings.latest_block.video_third,
        'docs': Doc.objects.all().order_by('?')[:5],
        'news': news,
        'twitts': twitts
    }


@register.inclusion_tag('partials/video_block.html')
def video_block(page_settings):
    return {
        'title': page_settings.video_block.title,
        'sub_title': page_settings.video_block.sub_title,
        'summary': page_settings.video_block.summary,
        'text': page_settings.video_block.text,
        'video': page_settings.video_block.video_obj,
    }


@register.inclusion_tag('partials/text_photo_block.html')
def text_photo_block(page_settings):
    if page_settings.text_photo_block:
        ctx = {
            'title': page_settings.text_photo_block.title,
            'sub_title': page_settings.text_photo_block.sub_title,
            'sub_sub_title': page_settings.text_photo_block.sub_sub_title,
            'top_text': page_settings.text_photo_block.top_text,
            'left_photo': page_settings.text_photo_block.left_photo,
            'left_photo_caption':
                page_settings.text_photo_block.left_photo_caption,
            'right_text': page_settings.text_photo_block.right_text,
            'middle_text': page_settings.text_photo_block.middle_text,
            'right_photo': page_settings.text_photo_block.right_photo,
            'right_photo_caption':
                page_settings.text_photo_block.right_photo_caption,
            'left_text': page_settings.text_photo_block.left_text,
            'bottom_text': page_settings.text_photo_block.bottom_text
        }
    else:
        ctx = {
            'title': page_settings.text_block.title,
            'sub_title': page_settings.text_block.sub_title,
            'text_elements': page_settings.text_block.text_element.all()
        }
    return ctx


@register.inclusion_tag('partials/expandable_section_block.html')
def expandable_section_block(page_settings):
    return {
        'title': page_settings.expandable_section_block.title,
        'description': page_settings.expandable_section_block.description,
        'sections': page_settings.expandable_section_block.section.all(),
    }


@register.inclusion_tag('partials/product_filter_acc_block.html',
                        takes_context=True)
def wizard_product_found_block(context, page_settings):
    sort_params, touch, q = \
        serialize_sort_data(context.get('request').GET.dict())
    if touch == 'True':
        queryset = Product.objects.filter(
            **{
                'category__country_flag__abbreviation':
                    context.get('request').country,
                'touch__isnull': False
            })
    elif touch == 'False':
        queryset = Product.objects.filter(
            **{
                'category__country_flag__abbreviation':
                    context.get('request').country,
                'touch__isnull': True
            })
    else:
        queryset = Product.objects.filter(
            category__country_flag__abbreviation=
            context.get('request').country)

    if sort_params.get('category__technology__id'):
        technology = Technology.objects.get(
            id=sort_params.get('category__technology__id'))
        context['technology'] = technology.name

    page = 1
    if sort_params.get('page'):
        page = sort_params.get('page')

    if sort_params.get('s'):
        order = sort_params.get('s')
    else:
        order = '-name'

    for i in ['q', 's', 'page']:
        if i in sort_params:
            sort_params.pop(i)

    context['products'] = queryset.filter(
        reduce(operator.and_, (Q(name__contains=x) for x in q.split(' ')))
        ).filter(**sort_params)

    context['products'] = context['products'].order_by(order)
    context['products_count'] = context['products'].order_by(order).count()
    paginated_objs = Paginator(context['products'], 11)

    context['num_pages'] = calculate_paginate(
        list(paginated_objs.page_range), page)
    try:
        context['products'] = paginated_objs.page(page).object_list
    except EmptyPage:
        context['products'] = paginated_objs.page(1).object_list
    context['technologies'] = Technology.objects.all()

    context['tft_interfaces'] = TftIF.INTERFACE_TYPE
    return context


@register.inclusion_tag('partials/product_filter_acc_block.html',
                        takes_context=True)
def bespoke_orders_block(context, page_settings):
    get_in_touch = GetInTouchBlock.objects.first()
    context.update({
        'technologies': Technology.objects.all(),
        'touches': Touch.objects.all(),
        'tft_interfaces': TftIF.INTERFACE_TYPE
    })
    if get_in_touch:
        context.update(
            {
                'call_us_title': get_in_touch.call_us_title,
                'call_us_description': get_in_touch.call_us_description,
                'chat_us_title': get_in_touch.chat_title,
                'chat_us_description': get_in_touch.chat_description,
                'email_us_title': get_in_touch.email_title,
                'email_us_description': get_in_touch.email_description,
                'email_us_form': ContactRequestCreate,
                'addresses': Address.objects.all()
            }
        )
    return context


@register.inclusion_tag('partials/product_detail_block.html',
                        takes_context=True)
def product_detail_block(context, page_settings):
    context['product'] = get_object_or_404(
        Product, id=context.get('product_id', 1))
    return context


@register.inclusion_tag('partials/product_category_block.html',
                        takes_context=True)
def product_category_block(context, page_settings):
    if page_settings.product_category_block.is_service_list:
        ctx = {
            'technologies': Service.objects.all(),
            'services': 'services', 'path': 'services',
        }
    else:
        ctx = {
            'technologies': Technology.objects.all(),
            'products': 'products', 'path': 'products',
            'is_detail_list':
                page_settings.product_category_block.is_detail_list,
            'country': CountryFlag.objects.get(
                abbreviation=context.request.country)
        }
    return ctx


@register.inclusion_tag('partials/our_people_block.html')
def our_people_block(page_settings):
    return {
        'teams': Team.objects.all(),
        'head_text': page_settings.our_people_block.head_text
    }


@register.inclusion_tag('partials/product_subcategory_block.html',
                        takes_context=True)
def product_subcategory_block(context, page_settings):
    ctx = {}
    if 'technology' in context:
        ctx = {
            'technology': get_object_or_404(
                Technology, id=context['technology_name']),
            'country': CountryFlag.objects.get(
                abbreviation=context.request.country)
        }
    elif 'service' in context:
        ctx = {
            'service': get_object_or_404(Service, id=context['service']),
        }
    return ctx


@register.inclusion_tag('partials/search_block.html', takes_context=True)
def search_block(context, page_settings):
    url = resolve(context.request.path_info)
    page = context.get('request').GET.get('page', 1)
    data = {
        'title': page_settings.search_block.name,
        'help_text': page_settings.search_block.help_text,
        'search_name': context.request.GET.get('q', ''),
    }
    if url.url_name == 'search_results':
        keys = context.request.GET.get('q', '').split(' ')

        category = \
            Category.objects.filter(
                reduce(operator.or_, (Q(name__contains=x) for x in keys))
            ) | \
            Category.objects.filter(
                reduce(operator.and_, (
                    Q(description__contains=x) for x in keys)))

        technology = \
            Technology.objects.filter(
                reduce(operator.or_, (Q(name__contains=x) for x in keys))
            ) | \
            Technology.objects.filter(
                reduce(operator.and_, (
                    Q(description__contains=x) for x in keys)))

        service = \
            Service.objects.filter(
                reduce(operator.or_, (Q(name__contains=x) for x in keys))
            ) | \
            Service.objects.filter(
                reduce(operator.and_, (
                    Q(description__contains=x) for x in keys)))

        sub_service = \
            SubService.objects.filter(
                reduce(operator.or_, (Q(name__contains=x) for x in keys))
            ) | \
            SubService.objects.filter(
                reduce(operator.and_, (
                    Q(description__contains=x) for x in keys)))

        paginated_products = Paginator(
            list(chain(technology, category)), 12)
        paginated_services = Paginator(
            list(chain(service, sub_service)), 12)

        product_page = page \
            if int(page) <= list(paginated_products.page_range)[-1] \
            else list(paginated_products.page_range)[-1]
        services_page = page \
            if int(page) <= list(paginated_services.page_range)[-1] \
            else list(paginated_services.page_range)[-1]

        items = OrderedDict([
            ('Products', paginated_products.page(product_page).object_list),
            ('Services', paginated_services.page(services_page).object_list),
        ])

        num_items = calculate_paginate(
            max(list(paginated_products.page_range),
                list(paginated_services.page_range), key=len),
            context.get('request').GET.get('page', 1))

        data['page'] = page
        data['results'] = \
            technology.count() + category.count() +\
            service.count() + sub_service.count()
        data['num_items'] = num_items
        data['items'] = items
    return data


@register.inclusion_tag('partials/browse_block.html', takes_context=True)
def browse_block(context, page_settings):
    browse = context.get('request').GET.get('browse', 'all')
    q = context.get('request').GET.get('q', '')

    faq_queryset = \
        FAQ.objects.filter(
            reduce(operator.and_, (Q(name__contains=x) for x in q.split(' ')))
        ) | \
        FAQ.objects.filter(
            reduce(operator.and_, (
                Q(description__contains=x) for x in q.split(' '))))

    doc_queryset = \
        Doc.objects.filter(
            reduce(operator.and_, (Q(name__contains=x) for x in q.split(' ')))
        ) | \
        Doc.objects.filter(
            reduce(operator.and_, (
                Q(description__contains=x) for x in q.split(' '))))

    video_queryset = \
        VideoObject.objects.filter(
            reduce(operator.and_, (Q(name__contains=x) for x in q.split(' ')))
        ) | \
        VideoObject.objects.filter(
            reduce(operator.and_, (
                Q(description__contains=x) for x in q.split(' ')))
        ) | \
        VideoObject.objects.filter(
            reduce(operator.and_, (
                Q(sub_name__contains=x) for x in q.split(' '))))

    if browse != 'all':
        browse = Technology.objects.get(id=browse)
        paginated_faqs = Paginator(
            faq_queryset.filter(category__technology_id=browse), 4)
        paginated_docs = Paginator(
            doc_queryset.filter(category__technology_id=browse), 4)
        paginated_videos = Paginator(video_queryset.filter(
            category__technology_id=browse), 3)
    else:
        paginated_faqs = Paginator(faq_queryset.all(), 4)
        paginated_docs = Paginator(doc_queryset.all(), 4)
        paginated_videos = Paginator(video_queryset.all(), 3)
    faqs = paginated_faqs.page(
        context.get('request').GET.get('faqs', 1)).object_list
    docs = paginated_docs.page(
        context.get('request').GET.get('docs', 1)).object_list
    videos = paginated_videos.page(
        context.get('request').GET.get('videos', 1)).object_list
    num_faqs = calculate_paginate(
        list(paginated_faqs.page_range),
        context.get('request').GET.get('faqs', 1))
    num_docs = calculate_paginate(
        list(paginated_docs.page_range),
        context.get('request').GET.get('docs', 1))
    num_videos = calculate_paginate(
        list(paginated_videos.page_range),
        context.get('request').GET.get('videos', 1))

    return {
        'title': page_settings.browse_block.name,
        'help_text': page_settings.browse_block.help_text,
        'categories': Technology.objects.all(),
        'browse': browse,
        'faqs': faqs,
        'docs': docs,
        'main_video': videos[:1],
        'videos': videos[1:],
        'num_faqs': num_faqs,
        'num_docs': num_docs,
        'num_videos': num_videos,
        'cur_faqs': int(context.get('request').GET.get('faqs', 1)),
        'cur_docs': int(context.get('request').GET.get('docs', 1)),
        'cur_videos': int(context.get('request').GET.get('videos', 1))
    }


@register.inclusion_tag('partials/get_in_touch_block.html')
def get_in_touch_block(page_settings):
    return {
        'call_us_title': page_settings.get_in_touch_block.call_us_title,
        'call_us_description':
            page_settings.get_in_touch_block.call_us_description,

        'chat_us_title': page_settings.get_in_touch_block.chat_title,
        'chat_us_description':
            page_settings.get_in_touch_block.chat_description,

        'email_us_title': page_settings.get_in_touch_block.email_title,
        'email_us_description':
            page_settings.get_in_touch_block.email_description,
        'email_us_form': ContactRequestCreate,
        'addresses': Address.objects.all()
    }


@register.inclusion_tag('partials/contact_box.html')
def contact_block(page_settings):
    return {
        'contact_detail_title':
            page_settings.contact_block.contact_detail_title,
        'contact_detail_sub_title':
            page_settings.contact_block.contact_detail_sub_title,
        'contact_detail_help_text':
            page_settings.contact_block.contact_detail_help_text,
        'contact_form_title':
            page_settings.contact_block.contact_form_title,
        'contact_form_sub_title':
            page_settings.contact_block.contact_form_sub_title,
        'contact_form_text':
            page_settings.contact_block.contact_form_text,
        'contact_form_success_text':
            page_settings.contact_block.contact_form_success_text,
        'email_us_form': ContactRequestCreate,
        'addresses': Address.objects.all()
    }


@register.inclusion_tag('partials/news_box.html', takes_context=True)
def news_block(context, page_settings):
    sort_params = {}
    months = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July',
        'August', 'September', 'October', 'November', 'December'
    ]
    news = News.objects.filter(publicated__isnull=False)
    last_new = news.order_by('publicated').last()
    year = context.get('request').GET.get('year', None)
    month_name = context.get('request').GET.get(
        'month', None)
    month = months.index(month_name) + 1\
        if str(month_name) != 'None' else None

    day = context.get('request').GET.get('day', None)
    set_if_not_none(sort_params, 'publicated__day', day)
    set_if_not_none(sort_params, 'publicated__month', month)
    set_if_not_none(sort_params, 'publicated__year', year)
    map = get_news_map(news)
    sorted_news = news.filter(**sort_params).order_by('-publicated')
    if 'id' in context:
        new = News.objects.get(id=context.get('id', 1))
        return {
            'new': new,
            'sorted_news': sorted_news,
            'map': map,
            'year': year,
            'month': month_name,
            'day': day,
            'request': context.request
        }

    paginated_news = Paginator(sorted_news, 5)
    news = paginated_news.page(
        context.get('request').GET.get('page', 1)).object_list
    num_news = calculate_paginate(
        list(paginated_news.page_range),
        context.get('request').GET.get('page', 1))

    return {
        'news': news,
        'sorted_news': news,
        'map': map,
        'cur_news': context.get('request').GET.get('page', 1),
        'num_news': num_news,
        'year': year,
        'month': month_name,
        'day': day,
    }


@register.inclusion_tag('partials/evaluation_kit_block.html',
                        takes_context=True)
def evaluation_kit_block(context, page_settings):
    return {
        'kit': EvaluationKit.objects.get(
            product__id=context.get('product_id', 1)),
        'evaluation_kit_block': page_settings.evaluation_kit_block,
        'product': Product.objects.get(id=context.get('product_id'))
    }


@register.inclusion_tag('partials/footer.html')
def footer_block(page_settings):
    return {
        'top_links': page_settings.footer_block.top_links.order_by(
            'priority'),
        'contact': page_settings.footer_block.contact,
        'top_contacts': page_settings.footer_block.contact_address.all(),
        'bot_copy_right': page_settings.footer_block.t_copy_right,
        'bot_link': page_settings.footer_block.a_link.order_by('priority'),
        'bot_back_top': page_settings.footer_block.a_back_top
    }


@register.inclusion_tag('partials/opportunities_block.html')
def opportunities_block(page_settings):
    items = Opportunity.objects.all().order_by('-added')
    return {
        'items': items[:3],
        'full_items': items
    }


def set_if_not_none(mapping, key, value):
    if value is not None:
        mapping[key] = value
