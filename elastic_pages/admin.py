from django.contrib import admin

from densitron.admin import admin_site

from .models import Page, PageHeaderBlock, PageHeadDropMenu, \
    PageHeadDropMenuElement, PageHelpBoxBlock, PageMainBlock, \
    PageFooterBlock, PageHeadSocLink, PageButton, PageWhatYouNeedBlock, \
    PageWorldPayScreenBlock, SlideElement, PostsGalleryBlock, \
    BespokeScreenBlock, LatestBlock, VideoBlock, TextPhotoBlock, \
    ExpandableSectionBlock, TextBlock, TextElement, ProductDetailBlock,\
    OurPeopleBlock, VideoObject, GetInTouchBlock, PageCategoryBlock, \
    PageSubCategoryBlock, SearchBlock, BrowseBlock, ContactBlock, NewsBlock,\
    ExpandableSection, EvaluationKitBlock, Bullet, OpportunitiesBlock, \
    WizardProductFoundBlock


class PageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'page_type', 'page_url', 'is_current_page')


class PageHeaderBlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_image', 'is_auth_menu')


class PageHeadDropMenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'external_link', 'priority', 'is_target_link')


class PageHeadDropMenuElementAdmin(admin.ModelAdmin):
    list_display = ('title', 'external_link', 'priority', 'is_target_link')


admin_site.register(Page, PageAdmin)
admin_site.register(PageHeaderBlock, PageHeaderBlockAdmin)
admin_site.register(PageHeadDropMenu, PageHeadDropMenuAdmin)
admin_site.register(PageHeadDropMenuElement, PageHeadDropMenuElementAdmin)
admin_site.register(PageHelpBoxBlock)
admin_site.register(PageMainBlock)
admin_site.register(PageFooterBlock)
admin_site.register(PageHeadSocLink)
admin_site.register(PageButton)
admin_site.register(PageWhatYouNeedBlock)
admin_site.register(PageWorldPayScreenBlock)
admin_site.register(SlideElement)
admin_site.register(PostsGalleryBlock)
admin_site.register(BespokeScreenBlock)
admin_site.register(LatestBlock)
admin_site.register(ExpandableSectionBlock)
admin_site.register(ExpandableSection)
admin_site.register(Bullet)
admin_site.register(VideoBlock)
admin_site.register(TextPhotoBlock)
admin_site.register(TextBlock)
admin_site.register(TextElement)
admin_site.register(ProductDetailBlock)
admin_site.register(OurPeopleBlock)
admin_site.register(VideoObject)
admin_site.register(GetInTouchBlock)
admin_site.register(PageCategoryBlock)
admin_site.register(PageSubCategoryBlock)
admin_site.register(SearchBlock)
admin_site.register(BrowseBlock)
admin_site.register(ContactBlock)
admin_site.register(NewsBlock)
admin_site.register(EvaluationKitBlock)
admin_site.register(OpportunitiesBlock)