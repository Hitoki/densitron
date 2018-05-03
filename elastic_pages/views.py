import csv
import datetime

from django.core.urlresolvers import resolve, reverse
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.syndication.views import Feed

from contacts.models import ContactRequest
from products.models import News


def handler404(request):
    return render(request, '404.html', {})


class Test404View(TemplateView):
    template_name = '404.html'

    def get(self, request, *args, **kwargs):
        from elastic_pages.models import Page
        page = get_object_or_404(
            Page, page_type=resolve(self.request.path_info).url_name,
            is_current_page=True)
        context = self.get_context_data(page, **kwargs)
        return self.render_to_response(context)

    def get_context_data(self, page, **kwargs):
        context = super(Test404View, self).get_context_data(**kwargs)
        context['page_settings'] = page
        return context


class GlobalView(TemplateView):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        from elastic_pages.models import Page
        url = resolve(self.request.path_info)
        if url.kwargs.get('special_name') == 'media':
            page = ''
        elif url.url_name == 'special-special_page' or url.url_name \
                == 'special-special_2_page':
            page_url = '/{}/'.format(url.kwargs.get('special_name'))
            if 'special_2_name' in url.kwargs:
                page_url = '/{}/{}/'.format(url.kwargs.get('special_name'),
                                            url.kwargs.get('special_2_name'))
            page = get_object_or_404(Page, page_url=page_url,
                                     is_current_page=True)
        else:
            page = get_object_or_404(
                Page,
                page_type__endswith=resolve(
                    self.request.path_info).url_name.split('-')[-1],
                is_current_page=True, page_url='')
        context = self.get_context_data(page, **kwargs)
        return self.render_to_response(context)

    def get_extra_context(self, context, page, **kwargs):
        if page.page_type == 'product-product_detail':
            context['product_id'] = kwargs.get('product_id', None)
        elif page.page_type == 'product-technology_detail':
            context['technology_name'] = kwargs.get('technology', None)
            context['service'] = kwargs.get('service', None)
        return context

    def get_context_data(self, page, **kwargs):
        context = super(GlobalView, self).get_context_data(**kwargs)
        context['page_settings'] = page
        if page:
            context = self.get_extra_context(context, page, **kwargs)
        return context


class RssSiteNewsFeed(Feed):
    title = "Densitron site news"
    link = "company/news/"
    description = "Updates on changes and additions to police beat central."

    def items(self):
        return News.objects.order_by('-publicated')[:20]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.get_short_text()

    def item_link(self, item):
        return reverse('company-news_detail', args=[item.pk])


def csv_export(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = \
        'attachment; filename="Request contacts - {}.csv"'\
        .format(datetime.datetime.now().isoformat())
    contact_requests = ContactRequest.objects.all()
    head = [i.name.replace('_', ' ').capitalize() for i
            in ContactRequest._meta.fields]
    writer = csv.writer(response)
    writer.writerow(head)
    for contact in contact_requests:
        data = [contact.serializable_value(i.name) for i
                in ContactRequest._meta.fields]
        writer.writerow(data)
    return response



