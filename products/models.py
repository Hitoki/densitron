"""Module Products models
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Product - base model of product.
* Technology - base model of product technology.
* Touch - base model of product touch type.

"""

from django.db import models

from products.serializers import get_serialized_product_info

__all__ = ['Product', 'Technology', 'Touch', 'Feature']


class Feature(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Product(models.Model):
    POPULARITY_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey('Category')
    price = models.DecimalField(max_digits=14, decimal_places=2, default=0)

    size = models.CharField(max_length=18, verbose_name='Size (inches)')
    dimension_w = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    dimension_h = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    dimension_d = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    active_area_w = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    active_area_h = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    viewing_area_w = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    viewing_area_h = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)

    # OLED
    controller = models.ForeignKey(
        'Controller', null=True, blank=True, verbose_name='Controller')
    interface = models.ManyToManyField(
        'Interface', blank=True, verbose_name='Interface')

    # TFT
    colour = models.NullBooleanField(default=None)
    resolution = models.CharField(
        max_length=16, null=True, blank=True, verbose_name='Resolution')
    resolution_w = models.SmallIntegerField(null=True, blank=True)
    resolution_h = models.SmallIntegerField(null=True, blank=True)
    brightness = models.IntegerField(null=True, blank=True,
                                     verbose_name='Brightness (cd/m2)')
    viewing_angle = models.CharField(
        max_length=16, null=True, blank=True,
        verbose_name='Viewing Angle (U/D/L/R)')
    touch = models.ForeignKey(
        'Touch', null=True, blank=True, verbose_name='Touch')
    tft_interface = models.ManyToManyField(
        'TftIF', blank=True, verbose_name='TFT Interface')
    features = models.ManyToManyField(
        Feature, blank=True, verbose_name='Features')

    # Touch
    structure = models.ForeignKey(
        'Structure', null=True, blank=True, verbose_name='Structure')
    touch_points = models.SmallIntegerField(
        null=True, blank=True, verbose_name='Touch Points')
    supported_os = models.ManyToManyField(
        'Os', blank=True, verbose_name='Supported Os')

    # Custom fields:

    popularity = models.CharField(
        max_length=1, choices=POPULARITY_CHOICES, default='3')
    why_dens = models.ManyToManyField(
        'Bullet', related_name='why_dens')
    commonly_used = models.ManyToManyField(
        'Bullet', related_name='commonly_used')
    commonly_used_in = models.ManyToManyField(
        'UsedIn', related_name='commonly_used_in', blank=True)
    spec = models.ForeignKey('Spec', null=True, blank=True,
                             on_delete=models.SET_NULL)
    application = models.ManyToManyField(
        'Application', blank=True, verbose_name='Applications')
    evaluation_kit = models.ForeignKey(
        'EvaluationKit', null=True, blank=True, verbose_name='Evaluation Kit')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_name(self):
        return '{}-{}'.format(self.category, self.name)

    def get_dimension(self):
        return '{} x {} x {}'.format(
            self.dimension_w, self.dimension_h, self.dimension_d)

    def get_resolution(self):
        area = None
        if self.resolution_w or self.resolution_h:
            area = '{} x {}'.format(self.resolution_w or '-',
                                    self.resolution_h or '-')
        return area

    def get_active_area(self):
        area = None
        if self.active_area_w or self.active_area_h:
            area = '{} x {}'.format(self.active_area_w or '-',
                                    self.active_area_h or '-')
        return area

    def get_viewing_area(self):
        area = None
        if self.viewing_area_w or self.viewing_area_h:
            area = '{} x {}'.format(self.viewing_area_w or '-',
                                    self.viewing_area_h or '-')
        return area

    def get_info_list(self):
        data = get_serialized_product_info(self)
        return data


class ProductImage(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(
        upload_to='images',
        help_text='Best size: 678 px / 396 px. Min-width: 248 px')
    product = models.ForeignKey('Product', blank=True, null=True)

    def __str__(self):
        return '{} of {}'.format(self.name, self.product.name)

    class Meta:
        verbose_name_plural = 'Product Images'


class OledProduct(Product):
    pass


class TftProduct(Product):
    pass


class TouchPanelProduct(Product):
    pass


class MonochromeProduct(Product):
    pass


class LowPowerProduct(Product):
    pass


class Technology(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    short_description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to='images',
        help_text='Best size: 640 px / 218 px. Min-height: 218 px.')
    thumbnail = models.ImageField(
        upload_to='images', null=True, blank=True,
        help_text=
        'Best size: 80 px / 80 px. Max-height: 80 px. Max-width: 160px.'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'

    def get_thumbnail(self):
        if self.thumbnail:
            image = self.thumbnail
        else:
            image = self.image
        return image


class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    technology = models.ForeignKey('Technology')
    commonly_used = models.ManyToManyField(
        'Bullet', related_name='commonly_used_category')
    commonly_used_in = models.ManyToManyField(
        'UsedIn', related_name='commonly_used_in_category', blank=True)
    image = models.ImageField(
        upload_to='images',
        help_text='Best size: 70 px / 70 px. Max-height: 70 px.')
    country_flag = models.ManyToManyField(
        'CountryFlag', related_name='country_flag', blank=True
    )
    priority = models.SmallIntegerField(
        default=1,
        help_text='Placing priority of the element among the same types, '
                  '1 - the first, 2 - of the second and so on.')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['priority']
        verbose_name = 'Product Sub-Category'
        verbose_name_plural = 'Product Sub-categories'


class TftIF(models.Model):
    RGB = 'RGB'
    LVDS = 'LVDS'
    HDMI = 'HDMI'
    USB = 'USB'
    MIPI = 'MIPI'
    DISPLAY_PORT = 'DPPT'
    MPU = 'MPU'
    DVI = 'DVI'
    SERIAL = 'SRL'
    INTERFACE_TYPE = (
        (RGB, 'RGB'),
        (LVDS, 'LVDS'),
        (HDMI, 'HDMI'),
        (USB, 'USB'),
        (MIPI, 'MIPI'),
        (DISPLAY_PORT, 'Display port'),
        (MPU, 'MPU'),
        (DVI, 'DVI'),
        (SERIAL, 'Serial'),
    )
    name = models.CharField(max_length=32)
    interface_type = models.CharField(
        max_length=4, choices=INTERFACE_TYPE, default='RGB')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class TouchIF(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Structure(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Controller(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Interface(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Os(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Touch(models.Model):
    type = models.CharField(max_length=128, verbose_name='Touch Type')
    touch_i_f = models.ForeignKey('TouchIF', null=True, blank=True)
    points = models.SmallIntegerField(default=1, verbose_name='Touch Points')

    def __str__(self):
        i_f_name = self.touch_i_f.name if self.touch_i_f else '-'
        return '{}/{}/{}'.format(self.type, i_f_name, self.points)


class Service(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    short_description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to='images',
        help_text='Best size: 640 px / 218 px. Min-height: 218 px.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def get_thumbnail(self):
        # if self.thumbnail:
        #     image = self.thumbnail
        # else:
        image = self.image
        return image


class SubService(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    technology = models.ForeignKey('Service')
    characteristic = models.ManyToManyField('Characteristic')
    why_densitron = models.ManyToManyField('Bullet',
                                           related_name='why_densitron')
    key_benefits = models.ManyToManyField('Bullet',
                                          related_name='key_benefits')
    image = models.ImageField(
        upload_to='images',
        help_text='Best size: 640 px / 218 px. Min-height: 218 px.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sub-category service'
        verbose_name_plural = 'Sub-category services'


class Bullet(models.Model):
    name = models.CharField(max_length=128)
    text = models.TextField()

    def __str__(self):
        return self.name


class Characteristic(models.Model):
    name = models.CharField(max_length=128)
    text = models.TextField(
        help_text='Add text as html code. For example')
    image = models.ImageField(
        upload_to='images', help_text='Best size: 415 px / 180 px.')
    is_view_image_button = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Doc(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    file = models.FileField(upload_to='docs', blank=True, null=True)
    category = models.ForeignKey('Category', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Doc'
        verbose_name_plural = 'Docs'


class FAQ(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    category = models.ForeignKey('Category', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'


class UsedIn(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(
        upload_to='images', help_text='Best size: 54 px / 45 px.')

    def __str__(self):
        return self.name


class Spec(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    file = models.FileField(upload_to='docs')

    def __str__(self):
        return self.name

    def get_size(self):
        if self.file.size < 512000:
            value = self.file.size / 1024.0
            ext = 'kb'
        elif self.file.size < 4194304000:
            value = self.file.size / 1048576.0
            ext = 'mb'
        else:
            value = self.file.size / 1073741824.0
            ext = 'gb'
        return '{}{}'.format(str(round(value, 2)), ext)


class BespokeOrder(models.Model):
    name = models.CharField(max_length=128)
    spec = models.TextField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Application(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(
        null=True, blank=True, upload_to="images",
        help_text=
        'Best size: 126 px / 100 px. Min-width: 126 px, Min-height: 100 px.'
    )

    def __str__(self):
        return self.title


class EvaluationKit(models.Model):
    title = models.CharField(max_length=128)
    overview = models.CharField(max_length=128)
    description = models.TextField()
    hardware_features = models.ManyToManyField(
        Feature, related_name='hardware_features', blank=True)
    software_features = models.ManyToManyField(
        Feature, related_name='software_features', blank=True)

    def __str__(self):
        return self.title


class News(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(
        help_text='Field for comments.', null=True, blank=True)

    title = models.CharField(max_length=128)
    top_text = models.TextField(null=True, blank=True)
    left_photo = models.ImageField(
        upload_to='images', null=True, blank=True,
        help_text=
        'Best size: 278 px / 209 px. Min-width: 278 px, Min-height: 209 px.')
    left_photo_caption = models.CharField(
        max_length=128, null=True, blank=True)
    middle_text = models.TextField(null=True, blank=True)
    right_photo = models.ImageField(
        upload_to='images', null=True, blank=True,
        help_text=
        'Best size: 278 px / 209 px. Min-width: 278 px, Min-height: 209 px.')
    right_photo_caption = models.CharField(
        max_length=128, null=True, blank=True)
    bottom_text = models.TextField(null=True, blank=True)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publicated = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.name

    def get_short_text(self):
        if self.top_text:
            text = self.top_text
        elif self.middle_text:
            text = self.middle_text
        else:
            text = self.bottom_text
        return text


class Twitt(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    link = models.URLField(help_text='Link to the Twitter message')
    publicated = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class CountryFlag(models.Model):
    name = models.CharField(max_length=128)
    abbreviation = models.CharField(max_length=4)

    def __str__(self):
        return self.name


class AlphanumericOLED(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    display_id = models.IntegerField(default=0)
    category = models.ForeignKey('Category', null=True, blank=True)
    module = models.CharField(max_length=128)
    controller = models.CharField(max_length=128, null=True, blank=True)
    character_width = models.SmallIntegerField(default=0)
    character_height = models.SmallIntegerField(default=0)

    dimension_width = models.DecimalField(
        default=0, max_digits=6, decimal_places=2)
    dimension_height = models.DecimalField(
        default=0, max_digits=6, decimal_places=2)
    dimension_depth = models.DecimalField(
        default=0, max_digits=6, decimal_places=2)
    viewing_area_width = models.DecimalField(
        default=0, max_digits=6, decimal_places=2)
    viewing_area_height = models.DecimalField(
        default=0, max_digits=6, decimal_places=2)

    active_area_width = models.DecimalField(
        default=0, max_digits=6, decimal_places=2)
    active_area_height = models.DecimalField(
        default=0, max_digits=6, decimal_places=2)

    # character_size (in tft)
    screen_size = models.DecimalField(
        default=0, max_digits=6, decimal_places=2)
    screen_diagonal = models.DecimalField(
        default=0, max_digits=6, decimal_places=2)

    package_mode = models.CharField(max_length=128, null=True, blank=True)
    duty = models.CharField(max_length=128, null=True, blank=True)

    backlight_optional = models.BooleanField(default=False)
    el = models.BooleanField(default=False)
    edge_led = models.BooleanField(default=False)
    smd_led = models.BooleanField(default=False)
    cfl = models.BooleanField(default=False)
    cfl_direct = models.BooleanField(default=False,)

    # size " (in tft)
    tft_size = models.DecimalField(
        default=0, max_digits=6, decimal_places=2)
    tft_mode = models.CharField(max_length=128, null=True, blank=True)
    # bright (in tft)
    tft_brightness = models.SmallIntegerField(default=0)

    interface = models.CharField(max_length=128)

    # backlight
    tft_backlight = models.CharField(max_length=256, null=True, blank=True)
    tft_driving_board = models.CharField(max_length=256, null=True, blank=True)
    tft_driving_board_link = models.CharField(
        max_length=256, null=True, blank=True)
    # resolution
    tft_resolution = models.CharField(max_length=256, null=True, blank=True)

    popup_text = models.CharField(max_length=256, null=True, blank=True)
    display_country = models.SmallIntegerField(default=0)
    display_country_include = models.BooleanField(default=True)

    # Custom fields For OLED [Null, Null, False] -----------------------------
    custom_field_1 = models.CharField(max_length=256, null=True, blank=True)
    custom_field_1_text = models.TextField(null=True, blank=True)
    custom_field_1_set = models.BooleanField(default=False)

    custom_field_2 = models.CharField(max_length=256, null=True, blank=True)
    custom_field_2_text = models.TextField(null=True, blank=True)
    custom_field_2_set = models.BooleanField(default=False)

    custom_field_3 = models.CharField(max_length=256, null=True, blank=True)
    custom_field_3_text = models.TextField(null=True, blank=True)
    custom_field_3_set = models.BooleanField(default=False)

    custom_field_4 = models.CharField(max_length=256, null=True, blank=True)
    custom_field_4_text = models.TextField(null=True, blank=True)
    custom_field_4_set = models.BooleanField(default=False)

    custom_field_5 = models.CharField(max_length=256, null=True, blank=True)
    custom_field_5_text = models.TextField(null=True, blank=True)
    custom_field_5_set = models.BooleanField(default=False)

    custom_field_6 = models.CharField(max_length=256, null=True, blank=True)
    custom_field_6_text = models.TextField(null=True, blank=True)
    custom_field_6_set = models.BooleanField(default=False)

    custom_field_7 = models.CharField(max_length=256, null=True, blank=True)
    custom_field_7_text = models.TextField(null=True, blank=True)
    custom_field_7_set = models.BooleanField(default=False)

    custom_field_8 = models.CharField(max_length=256, null=True, blank=True)
    custom_field_8_text = models.TextField(null=True, blank=True)
    custom_field_8_set = models.BooleanField(default=False)
    # ------------------------------------------------------------------------

    pdf_replacement_ektron_content_id = models.CharField(
        max_length=256, null=True, blank=True)
    pdf_replacement_ektron_content_id_tabs = models.CharField(
        max_length=256, null=True, blank=True)

    # Or FK to something, just now they are - Small Integer Field. -----------
    parent_id = models.SmallIntegerField(default=3)
    display_type = models.SmallIntegerField(default=1)
    ektron_content_id = models.SmallIntegerField(default=64)
    # ------------------------------------------------------------------------

    image_url = models.ImageField(null=True, blank=True)

    country_flag = models.SmallIntegerField(default=0)
    country_include = models.BooleanField(default=True)
    pdf_flag = models.SmallIntegerField(default=1)
    pdf_country_include = models.BooleanField(default=False)

    # Custom parameters ------------------------------------------------------
    why_dens = models.ManyToManyField(
        'Bullet', related_name='alphanumeric_oled_why_dens')
    commonly_used = models.ManyToManyField(
        'Bullet', related_name='alphanumeric_oled_commonly_used')
    commonly_used_in = models.ManyToManyField(
        'UsedIn', related_name='alphanumeric_oled_commonly_used_in',
        blank=True)
    spec = models.ForeignKey('Spec', null=True, blank=True)
    application = models.ManyToManyField('Application', blank=True)

    def __str__(self):
        return self.name
