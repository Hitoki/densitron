"""Module Elastic Pages models
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Page - model of elastic page.
* PageHeaderBlock - model of header block for Page.
* PageHeadSocLink - model of social link for PageHeaderBlock.
* PageHeadDropMenu - model of drop head bar link for PageHeaderBlock.
* PageHeadDropMenuElement - model of drop down link for PageHeadDropMenu.

* PageContentBlock - model of components for elastic page.


Example:
    Main Page [Page] = (
        Header         [ PageHeaderBlock ] +
        Help Box       [ PageHelpBoxBlock ] +
        Content        [ PageMainBlock ] +
        Footer         [ PageFooterBlock ]
    )
"""

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from elastic_pages.snippets import get_choice_patterns
from products.models import Category

__all__ = ['Page', 'PageHeaderBlock', 'PageHeadDropMenu',
           'PageHeadDropMenuElement', 'PageHelpBoxBlock',
           'PageMainBlock', 'PageFooterBlock', 'PageHeadSocLink',
           'PageWhatYouNeedBlock', 'PageWorldPayScreenBlock']


class Page(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')
    page_type = models.CharField(
        max_length=32, choices=tuple(get_choice_patterns()),
        default='home',
        help_text='Page type, select from the available list, '
                  'there can be only one instance of page for one type.')
    page_url = models.CharField(
        null=True, blank=True, max_length=255,
        help_text='It has higher priority than the page type, that defines '
                  'the path to the current page. Also, one page at a time '
                  'may be only one page. '
                  'To select the current need to enable Is current page.')
    is_current_page = models.BooleanField(
        default=False,
        help_text='Assign this page as a current (It will display). '
                  'All other pages with the same type automatically become '
                  'secondary.'
    )
    title = models.CharField(
        max_length=64,
        help_text="Defines a title in the browser toolbar, "
                  "provides a title for the page when it is added to "
                  "favorites and displays a title for "
                  "the page in search-engine results")
    extra_meta_data = models.TextField(null=True, blank=True)
    header_block = models.ForeignKey(
        'PageHeaderBlock', null=True, blank=True)
    get_in_touch_block = models.ForeignKey(
        'GetInTouchBlock', null=True, blank=True)
    help_box_block = models.ForeignKey(
        'PageHelpBoxBlock', null=True, blank=True)
    main_block = models.ForeignKey(
        'PageMainBlock', null=True, blank=True)
    our_people_block = models.ForeignKey(
        'OurPeopleBlock', null=True, blank=True)
    product_category_block = models.ForeignKey(
        'PageCategoryBlock', null=True, blank=True)
    product_subcategory_block = models.ForeignKey(
        'PageSubCategoryBlock', null=True, blank=True)
    product_detail_block = models.ForeignKey(
        'ProductDetailBlock', null=True, blank=True)
    wizard_product_found_block = models.ForeignKey(
        'WizardProductFoundBlock', null=True, blank=True)
    what_you_need_block = models.ForeignKey(
        'PageWhatYouNeedBlock', null=True, blank=True)
    worldpay_slide_block = models.ForeignKey(
        'PageWorldPayScreenBlock', null=True, blank=True)
    posts_gallery_block = models.ForeignKey(
        'PostsGalleryBlock', null=True, blank=True)
    bespoke_screen_block = models.ForeignKey(
        'BespokeScreenBlock', null=True, blank=True)
    bespoke_orders_block = models.ForeignKey(
        'BespokeOrdersBlock', null=True, blank=True)
    video_block = models.ForeignKey(
        'VideoBlock', null=True, blank=True)
    text_photo_block = models.ForeignKey(
        'TextPhotoBlock', null=True, blank=True)
    text_block = models.ForeignKey(
        'TextBlock', null=True, blank=True)
    contact_block = models.ForeignKey(
        'ContactBlock', null=True, blank=True)
    expandable_section_block = models.ForeignKey(
        'ExpandableSectionBlock', null=True, blank=True)
    news_block = models.ForeignKey(
        'NewsBlock', null=True, blank=True)
    evaluation_kit_block = models.ForeignKey(
        'EvaluationKitBlock', null=True, blank=True)
    opportunities_block = models.ForeignKey(
        'OpportunitiesBlock', null=True, blank=True)
    latest_block = models.ForeignKey(
        'LatestBlock', null=True, blank=True)
    search_block = models.ForeignKey(
        'SearchBlock', null=True, blank=True)
    browse_block = models.ForeignKey(
        'BrowseBlock', null=True, blank=True)
    footer_block = models.ForeignKey(
        'PageFooterBlock', null=True, blank=True)

    def __str__(self):
        return self.name


class PageHeaderBlock(models.Model):
    """PageHeaderBlock contains in itself the settings of this unit,
    it is also part of the Page
    Example:
    Main Header [PageHeaderBlock] = (
        Drop Down links             [ PageHeadDropMenu ] +
        Social Links                [ PageHeadSocLink ]
    )
    """
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')

    main_menus_elements = models.ManyToManyField(
        'PageHeadDropMenu', blank=True)
    is_auth_menu = models.BooleanField(
        default=True,
        help_text='It enables or disables the display dependent '
                  'of the authorization elements')
    logo_image = models.ImageField(
        upload_to='images',
        help_text=
        'Best size: 118 px / 67 px. Min-width: 118 px, Min-height: 67 px.')
    soc_links = models.ManyToManyField('PageHeadSocLink', blank=True)

    def __str__(self):
        return self.name


class PageHeadSocLink(models.Model):
    """PageHeadSocLink model for a social link,
    it is also part of the PageHeaderBlock
    Example:
    Main Header [PageHeaderBlock] = (
        Social Links [ Twitter [PageHeadSocLink]
                       FaceBook [PageHeadSocLink] ]
    )
    """
    name = models.CharField(max_length=128)

    soc_image = models.ImageField(
        upload_to='images',
        help_text=
        'Best size: 25 px / 25 px. Min-width: 25 px, Min-height: 25 px.')
    external_link = models.CharField(max_length=255)
    priority = models.SmallIntegerField(
        default=1,
        help_text='Placing priority of the element among the same types, '
                  '1 - the first, 2 - of the second and so on.')
    is_target_link = models.BooleanField(
        default=False,
        help_text='It enables or disables ability to open it in a new '
                  'browser window or a new tab.')

    def __str__(self):
        return self.name


class PageHeadDropMenu(models.Model):
    """PageHeadDropMenu model for a main header link bar,
    it can contain in itself links in drop down menu
    it is also part of the PageHeaderBlock
    Example:
    Main Header [PageHeaderBlock] = (
            [ PageHeadDropMenu ]     [ PageHeadDropMenu ]
        [[PageHeadDropMenuElement]]
        [[PageHeadDropMenuElement]]
        [[PageHeadDropMenuElement]]
    )
    """
    name = models.CharField(max_length=128)

    title = models.CharField(
        max_length=64,
        help_text='Displayed title of a link')
    external_link = models.CharField(
        null=True, blank=True, max_length=255,
        help_text='Fill it to add link to an external source, '
                  'its priority will be higher than the internal reference.')
    drop_links = models.ManyToManyField(
        'PageHeadDropMenuElement', blank=True)
    priority = models.SmallIntegerField(
        default=1,
        help_text='Placing priority of the element among the same types, '
                  '1 - the first, 2 - of the second and so on.')
    is_target_link = models.BooleanField(
        default=False,
        help_text='It enables or disables ability to open it in a new '
                  'browser window or a new tab.')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-priority']

    def get_link(self):
        """Get link function.
        Return demanding link

        :param self.external_link: External link
        :type self.external_link: str
        :param self.internal_link: Internal link
        :type self.external_link: str

        :return: External link if is it, unless there - '/' + Internal link
        :rtype: str
        """
        # link = self.external_link if self.external_link\
        #     else '/' + self.get_internal_link_display()
        link = self.external_link
        return link


class PageHeadDropMenuElement(models.Model):
    """PageHeadDropMenuElement model it is part of the PageHeaderBlock"""

    name = models.CharField(max_length=128)

    title = models.CharField(
        max_length=64,
        help_text='Displayed title of a link')
    external_link = models.CharField(
        null=True, blank=True, max_length=255,
        help_text='Fill it to add link to an external source, '
                  'its priority will be higher than the internal reference.')
    priority = models.SmallIntegerField(
        default=1,
        help_text='Placing priority of the element among the same types, '
                  '1 - the first, 2 - of the second and so on.')
    is_target_link = models.BooleanField(
        default=False,
        help_text='It enables or disables ability to open it in a new '
                  'browser window or a new tab.')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['priority']

    def get_link(self):
        """Get link function.
        Return demanding link

        :param self.external_link: External link
        :type self.external_link: str
        :param self.internal_link: Internal link
        :type self.external_link: str

        :return: External link if is it, unless there - '/' + Internal link
        :rtype: str
        """
        link = self.external_link
        return link


class PageHelpBoxBlock(models.Model):
    """PageHelpBoxBlock contains in itself the settings of this unit,
    it is also part of the Page
    """
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')

    text = models.TextField(
        help_text='Displayed text of a link (with safe template tag), '
                  'If you want to modify the text style, '
                  'wrap them in html tags. '
                  'b - <b>Bold</b>, i - <i>Italian</i>')
    button = models.ForeignKey('PageButton', blank=True, null=True)

    def __str__(self):
        return self.name


class PageButton(models.Model):
    """PageButton html button object model."""
    LEFT = 'L'
    RIGHT = 'R'
    BUTTON_POSITION_CHOICES = (
        (LEFT, 'Left'),
        (RIGHT, 'Right'),
    )

    ARROW = 'A'
    PLUS = 'P'
    BOX = 'B'
    BUTTON_TYPE_CHOICES = (
        (ARROW, 'Arrow'),
        (PLUS, 'Plus'),
        (BOX, 'Box'),
    )

    BLUE = 'B'
    GREEN = 'G'
    WHITE = 'W'
    ORANGE = 'O'
    COLOR_CHOICES = (
        (BLUE, 'Blue'),
        (GREEN,  'Green'),
        (WHITE,  'White'),
        (ORANGE,  'Orange'),
    )

    name = models.CharField(max_length=128)

    title = models.CharField(
        max_length=32,
        help_text='Displayed text of a link (with safe template tag), '
                  'If you want to modify the text style, '
                  'wrap them in html tags. '
                  'b - <b>Bold</b>, i - <i>Italian</i>')
    color = models.CharField(
        max_length=32, choices=COLOR_CHOICES, default=WHITE,
        help_text='Selection of the reserved color, that fills the '
                  'background for the button. Select the color you like, '
                  'border shadow and text color will change automatically.')
    glyphicon = models.CharField(
        max_length=1, default=ARROW, choices=BUTTON_TYPE_CHOICES,
        help_text='It changes the image of the glyphicon')
    glyphicon_position = models.CharField(
        max_length=1, default=RIGHT, choices=BUTTON_POSITION_CHOICES,
        help_text='It changes the position of the glyphicon, '
                  'to display it on the left side, pick Left.')
    external_link = models.CharField(
        null=True, blank=True, max_length=255,
        help_text='Fill it to add link to an external source, '
                  'its priority will be higher than the internal reference.')
    is_target_link = models.BooleanField(
        default=False,
        help_text='It enables or disables ability to open it in a new '
                  'browser window or a new tab.')

    def get_link(self):
        """Get link function.
        Return demanding link

        :param self.external_link: External link
        :type self.external_link: str
        :param self.internal_link: Internal link
        :type self.external_link: str

        :return: External link if is it, unless there - '/' + Internal link
        :rtype: str
        """
        link = self.external_link
        return link


class PageMainBlock(models.Model):
    """PageMainBlock contains in itself the settings of this unit,
    it is also part of the Page
    """
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')

    background_image = models.ImageField(
        upload_to='images',
        help_text='Best size: 640 px / 218 px. Min-height: 218 px.')

    title = models.CharField(max_length=128)
    text = models.TextField(
        help_text='Displayed text of a link (with safe template tag), '
                  'If you want to modify the text style, '
                  'wrap them in html tags. '
                  'b - <b>Bold</b>, i - <i>Italian</i>')

    def __str__(self):
        return self.name


class PageFooterBlock(models.Model):
    """PageFooterBlock contains in itself the settings of this unit,
    it is also part of the Page
    """
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')

    top_links = models.ManyToManyField(
        'PageHeadDropMenu', blank=True)

    contact = models.CharField(
        max_length=128, null=True, blank=True,
        help_text='The name of the column with addresses, '
                  'if left blank name field, contact column '
                  'will not be visible in the footer.')
    contact_address = models.ManyToManyField(
        'company.Address',
        help_text='Specify no more than 2 addresses simultaneously.')
    t_copy_right = models.CharField(
        max_length=255,
        help_text='Displayed copy right text, '
                  'If you want to modify the text style, '
                  'wrap them in html tags. '
                  'b - <b>Bold</b>, i - <i>Italian</i>')
    a_link = models.ManyToManyField(
        'PageHeadDropMenuElement', blank=True)
    a_back_top = models.BooleanField(
        default=False,
        help_text='It enables or disables button Back to Top')

    def __str__(self):
        return self.name


class PageWhatYouNeedBlock(models.Model):
    """PageWhatYouNeedBlock contains in itself the settings of this unit,
    it is also part of the Page
    """
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')

    title = models.CharField(max_length=128)

    left_column_title = models.CharField(max_length=64)
    is_touch = models.BooleanField(
        default=True,
        help_text='It enables or disables by Touch filter')
    is_colour = models.BooleanField(
        default=True,
        help_text='It enables or disables by Colour filter')

    middle_column_title = models.CharField(max_length=64)
    middle_column_label = models.CharField(max_length=64)
    middle_column_caption = models.CharField(max_length=64)

    right_column_title = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class PageWorldPayScreenBlock(models.Model):
    """PageWorldPayScreenBlock contains in itself the settings of this unit,
    it is also part of the Page
    """
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')

    slide_elem = models.ManyToManyField('SlideElement')
    auto_slide = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Slider panel'


class SlideElement(models.Model):
    """SlideElement model for PageWorldPayScreenBlock slide pages"""
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')

    title = models.CharField(max_length=128)
    text = models.TextField()
    background = models.ImageField(
        upload_to='images',
        help_text='The recommended size of image is 1440px/396px '
                  'But you can use any image sizes, they will be '
                  'compressed or increased to the appropriate value.')
    button = models.ForeignKey('PageButton', null=True, blank=True)

    def __str__(self):
        return self.name


class PostsGalleryBlock(models.Model):
    """PostsGalleryBlock contains in itself the settings of this unit,
    it is also part of the Page
    """
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')

    title_left = models.CharField(max_length=128)
    text_left = models.TextField()
    image_left = models.ImageField(
        upload_to='images',
        help_text='Best size for all images: 476 px / 266 px. ')
    link_left = models.CharField(max_length=255, null=True, blank=True)

    title_middle = models.CharField(max_length=128)
    text_middle = models.TextField()
    image_middle = models.ImageField(
        upload_to='images',
        help_text='Best size for all images: 476 px / 266 px. ')
    link_middle = models.CharField(max_length=255, null=True, blank=True)

    title_right = models.CharField(max_length=128)
    text_right = models.TextField()
    image_right = models.ImageField(
        upload_to='images',
        help_text='Best size for all images: 476 px / 266 px. ')
    link_right = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '3 Promo Panel'


class BespokeScreenBlock(models.Model):
    """BespokeScreenBlock contains in itself the settings of this unit,
    it is also part of the Page
    """
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')

    title_top = models.CharField(max_length=64)
    title_bottom = models.CharField(max_length=64)
    link = models.CharField(max_length=255, null=True, blank=True)
    background = models.ImageField(
        upload_to='images',
        help_text='Best size: 1440 px / 300 px. Min-width: 1440 px')
    button = models.ForeignKey('PageButton', null=True, blank=True)

    def __str__(self):
        return self.name


class LatestBlock(models.Model):
    """LatestBlock contains in itself the settings of this unit,
    it is also part of the Page
    """
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')
    video_main = models.ForeignKey(
        'VideoObject', null=True, blank=True, related_name='video_main')
    video_second = models.ForeignKey(
        'VideoObject', null=True, blank=True, related_name='video_second')
    video_third = models.ForeignKey(
        'VideoObject', null=True, blank=True, related_name='video_third')

    def __str__(self):
        return self.name


class VideoBlock(models.Model):
    """VideoBlock contains in itself the settings of this unit,
    it is also part of the Page
    """
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')

    title = models.CharField(max_length=128)
    sub_title = models.CharField(max_length=128)
    summary = models.CharField(max_length=128)
    text = models.TextField()
    video_obj = models.ForeignKey(
        'VideoObject', null=True, blank=True, related_name='video_obj')

    def __str__(self):
        return self.name


class TextPhotoBlock(models.Model):
    """TextPhotoBlock contains in itself the settings of this unit,
    it is also part of the Page
    """
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')

    title = models.CharField(max_length=128)
    sub_title = models.CharField(max_length=128)
    sub_sub_title = models.CharField(max_length=128)
    top_text = models.TextField()
    left_photo = models.ImageField(
        upload_to='images',
        help_text='Best size: 278 px / 206 px.')
    left_photo_caption = models.CharField(max_length=128)
    right_text = models.TextField()
    middle_text = models.TextField(null=True, blank=True)
    right_photo = models.ImageField(
        upload_to='images',
        help_text='Best size: 278 px / 206 px.')
    right_photo_caption = models.CharField(max_length=128)
    left_text = models.TextField()
    bottom_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class TextBlock(models.Model):
    """TextBlock contains in itself the settings of this unit,
    it is also part of the Page
    """
    name = models.TextField()
    description = models.TextField(help_text='Field for comments.')
    title = models.TextField()
    sub_title = models.TextField()
    text_element = models.ManyToManyField('TextElement')

    def __str__(self):
        return self.name


class TextElement(models.Model):
    """TextElement model for Text Block"""
    name = models.TextField()
    description = models.TextField(help_text='Field for comments.')
    sub_sub_title = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.name


class ExpandableSectionBlock(models.Model):
    """ExpandableSectionBlock contains in itself the settings of this unit,
    it is also part of the Page
    """
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')
    title = models.CharField(max_length=128)
    section = models.ManyToManyField('ExpandableSection')

    def __str__(self):
        return self.name


class ExpandableSection(models.Model):
    """ExpandableSection model for ExpandableSection Block"""
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')
    title = models.CharField(max_length=128)
    sub_title = models.CharField(max_length=128)
    sub_sub_title = models.CharField(max_length=128)
    text = models.TextField()
    bullet = models.ManyToManyField('Bullet')

    def __str__(self):
        return self.name


class Bullet(models.Model):
    """Bullet model for special holder them block"""
    GREEN_OKAY = 'G-Ok'
    STYLE_CHOICES = (
        (GREEN_OKAY,  "Green with 'Okay' ico"),
    )

    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')
    style = models.CharField(max_length=8, choices=STYLE_CHOICES,
                             default=GREEN_OKAY)
    title = models.CharField(max_length=128)
    text = models.TextField()

    def __str__(self):
        return self.name


class WizardProductFoundBlock(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')

    def __str__(self):
        return self.name


class ProductDetailBlock(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')

    def __str__(self):
        return self.name


class PageCategoryBlock(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')
    is_service_list = models.BooleanField(default=False,
                                          help_text="Display Service list")
    is_detail_list = models.BooleanField(
        default=True, help_text="Display Category list with subcategories")

    def __str__(self):
        return self.name


class PageSubCategoryBlock(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')
    is_service_list = models.BooleanField(default=False,
                                          help_text="Display Service list")

    def __str__(self):
        return self.name


class BespokeOrdersBlock(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')

    def __str__(self):
        return self.name


class OurPeopleBlock(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')
    head_text = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class VideoObject(models.Model):
    name = models.CharField(max_length=128)
    sub_name = models.CharField(max_length=128, null=True, blank=True)
    description = models.TextField(help_text='Field for comments.')
    video = models.FileField(upload_to='videos', null=True, blank=True)
    embed_video = models.CharField(max_length=256, null=True, blank=True)
    category = models.ForeignKey(Category, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_video(self):
        video = {}
        if self.video:
            video['video'] = self.video.url
        else:
            video['embed_video'] = self.embed_video
        return video


class GetInTouchBlock(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')
    call_us_title = models.CharField(max_length=128)
    call_us_description = models.TextField()

    chat_title = models.CharField(max_length=128)
    chat_description = models.TextField()

    email_title = models.CharField(max_length=128)
    email_description = models.TextField()

    def __str__(self):
        return self.name


class SearchBlock(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')
    help_text = models.TextField()

    def __str__(self):
        return self.name


class BrowseBlock(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')
    help_text = models.TextField()

    def __str__(self):
        return self.name


class ContactBlock(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')
    contact_detail_title = models.CharField(max_length=256)
    contact_detail_sub_title = models.CharField(max_length=256)
    contact_detail_help_text = models.TextField(null=True, blank=True)

    contact_form_title = models.CharField(max_length=256)
    contact_form_sub_title = models.CharField(max_length=256)
    contact_form_text = models.TextField(null=True, blank=True)
    contact_form_success_text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class NewsBlock(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(help_text='Field for comments.')
    is_detail_page = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class EvaluationKitBlock(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(
        help_text='Field for comments.', null=True, blank=True)
    title = models.CharField(max_length=128)
    instruction_text = models.TextField()

    def __str__(self):
        return self.name


class OpportunitiesBlock(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(
        help_text='Field for comments.', null=True, blank=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Page)
def set_other_pages_as_secondary(sender, instance, **kwargs):
    if instance.is_current_page and instance.page_url is None:
        sender.objects.filter(page_type=instance.page_type)\
            .exclude(id=instance.id).update(is_current_page=False)
    elif instance.page_url:
        sender.objects.filter(page_url=instance.page_url)\
            .exclude(id=instance.id).update(is_current_page=False)