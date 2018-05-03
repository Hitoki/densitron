from django.contrib import admin

from densitron.admin import admin_site

from contacts.models import ContactRequest, DownloadDocumentUserRequest


class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'head', 'user', 'date')
    readonly_fields = ('head', 'first_name', 'surname', 'email', 'country',
                       'phone', 'job_title', 'comments', 'user', 'date',
                       'to_email',)
    actions = ['export_csv']


class DownloadDocumentUserRequestAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'first_name', 'surname', 'email', 'doc_title')



admin_site.register(ContactRequest, ContactRequestAdmin)
admin_site.register(DownloadDocumentUserRequest,
                    DownloadDocumentUserRequestAdmin)
