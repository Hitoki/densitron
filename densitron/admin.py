from django.contrib.admin import AdminSite
from django.template.response import TemplateResponse
from django.conf.urls import url

from products.models import News, FAQ, Doc, ProductImage, Product, Category, \
    Technology, Service, SubService


class DensitronAdminSite(AdminSite):
    site_header = 'Densitron administration'

    def admin_special_view(
            self, request, app_label='document_and_media', **kwargs):
        name = kwargs.get('name', '')
        models = kwargs.get('models', [])
        app = {
            'app_label': app_label,
            'app_url': '/admin/'+app_label+'/',
            'name': name,
            'models': []
        }
        for model in models:
            app['models'].append({
                'object_name': model._meta.object_name,
                'name': model._meta.verbose_name_plural,
                'admin_url': '/admin/'+News._meta.app_label+'/'
                             +model._meta.object_name.lower()+'/',
                'add_url': '/admin/'+News._meta.app_label+'/'
                             +model._meta.object_name.lower()+'/add/',
            })
        context = dict(
            self.each_context(request),
            title=name,
            app_list=[app],
            app_label=app_label,
        )
        request.current_app = self.name
        return TemplateResponse(request, self.app_index_template or [
            'admin/%s/app_index.html' % app_label,
            'admin/app_index.html'
        ], context)

    def get_urls(self):
        urls = super(DensitronAdminSite, self).get_urls()
        urlpatterns = [
            url(r'^document_and_media/$', self.admin_special_view,
                {
                    'name': 'Document and Media',
                    'models': [News, Doc, FAQ, ProductImage]
                },
                name='app_list'),
            url(r'^products_and_services/$', self.admin_special_view,
                {
                    'name': 'Products & Services',
                    'models': [Product, Category, Technology, Service,
                               SubService]
                },
                name='app_list'),
        ]
        return urls + urlpatterns


admin_site = DensitronAdminSite(name='admin')
