from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

from densitron.admin import admin_site

from company.models import People, Team, Job, Admin, ContactUser,\
    Opportunity, Address


class AddressAdmin(admin.ModelAdmin):
    list_display = ('title', 'line_1', 'line_2', 'phone')


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('get_full_name', 'team', 'job', 'email', 'phone')


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'place_priority', )


class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'place_priority', )


class AdminAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'get_emails')


class ContactUserAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'phone')


class OpportunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'added', 'updated')


admin_site.register(Address, AddressAdmin)
admin_site.register(People, PeopleAdmin)
admin_site.register(Team, TeamAdmin)
admin_site.register(Job, JobAdmin)
admin_site.register(Admin, AdminAdmin)
admin_site.register(ContactUser, ContactUserAdmin)
admin_site.register(Opportunity, OpportunityAdmin)

admin_site.register(User, UserAdmin)
admin_site.register(Group)

