from django.contrib import admin

from densitron.admin import admin_site
from products.models import Feature, Technology, Category, \
    TftIF, Structure, Controller, Interface, Os, Touch, ProductImage, \
    Service, SubService, Bullet, Characteristic, Doc, FAQ, UsedIn, Spec,\
    BespokeOrder, Application, TouchIF, Product, News, EvaluationKit, Twitt


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'get_dimension', 'popularity')


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'thumbnail')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'technology', 'priority')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'image',)


class SubServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'technology',)

# In Product & Services admin section
admin_site.register(Product, ProductAdmin)
admin_site.register(Technology, TechnologyAdmin)
admin_site.register(Category, CategoryAdmin)
admin_site.register(Service, ServiceAdmin)
admin_site.register(SubService, SubServiceAdmin)

# In Product & Services Features admin section
admin_site.register(TftIF)
admin_site.register(Structure)
admin_site.register(Controller)
admin_site.register(Interface)
admin_site.register(Os)
admin_site.register(Touch)
admin_site.register(Feature)
admin_site.register(Characteristic)
admin_site.register(Bullet)
admin_site.register(UsedIn)
admin_site.register(Spec)
admin_site.register(BespokeOrder)
admin_site.register(Application)
admin_site.register(TouchIF)
admin_site.register(EvaluationKit)
admin_site.register(Twitt)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'added', 'updated', 'publicated',)


class FAQAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)


class DocAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'file',)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'product', 'image',)


# In Document and media admin section
admin_site.register(News, NewsAdmin)
admin_site.register(FAQ, FAQAdmin)
admin_site.register(Doc, DocAdmin)
admin_site.register(ProductImage, ProductImageAdmin)