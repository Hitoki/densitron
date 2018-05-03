# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-15 14:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0045_auto_20160315_1341'),
        ('company', '0010_auto_20160315_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='BespokeOrdersBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
            ],
        ),
        migrations.CreateModel(
            name='BespokeScreenBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('title_top', models.CharField(max_length=64)),
                ('title_bottom', models.CharField(max_length=64)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('background', models.ImageField(help_text='The recommended size of a image is 1024 x 278 px. But you can use any image sizes, they will be compressed or increased to the appropriate value.', upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='BrowseBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('help_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Bullet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('style', models.CharField(choices=[('G-Ok', "Green with 'Okay' ico")], default='G-Ok', max_length=8)),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('contact_detail_title', models.CharField(max_length=256)),
                ('contact_detail_sub_title', models.CharField(max_length=256)),
                ('contact_detail_help_text', models.TextField(blank=True, null=True)),
                ('contact_form_title', models.CharField(max_length=256)),
                ('contact_form_sub_title', models.CharField(max_length=256)),
                ('contact_form_text', models.TextField(blank=True, null=True)),
                ('contact_form_success_text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationKitBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, help_text='Field for comments.', null=True)),
                ('title', models.CharField(max_length=128)),
                ('instruction_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ExpandableSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('title', models.CharField(max_length=128)),
                ('sub_title', models.CharField(max_length=128)),
                ('sub_sub_title', models.CharField(max_length=128)),
                ('text', models.TextField()),
                ('bullet', models.ManyToManyField(to='elastic_pages.Bullet')),
            ],
        ),
        migrations.CreateModel(
            name='ExpandableSectionBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('title', models.CharField(max_length=128)),
                ('section', models.ManyToManyField(to='elastic_pages.ExpandableSection')),
            ],
        ),
        migrations.CreateModel(
            name='GetInTouchBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('call_us_title', models.CharField(max_length=128)),
                ('call_us_description', models.TextField()),
                ('chat_title', models.CharField(max_length=128)),
                ('chat_description', models.TextField()),
                ('email_title', models.CharField(max_length=128)),
                ('email_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LatestBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
            ],
        ),
        migrations.CreateModel(
            name='NewsBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('is_detail_page', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OurPeopleBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('head_text', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('page_type', models.CharField(choices=[('company-about_us', 'Company-About Us'), ('company-company_detail', 'Company-Company Detail'), ('company-news', 'Company-News'), ('company-news_detail', 'Company-News Detail'), ('company-our_people', 'Company-Our People'), ('contact', 'Contact'), ('home', 'Home'), ('knowledge-base', 'Knowledge-Base'), ('privacy', 'Privacy'), ('product-product_detail', 'Product-Product Detail'), ('product-product_detail_kit', 'Product-Product Detail Kit'), ('product-technology', 'Product-Technology'), ('product-technology_detail', 'Product-Technology Detail'), ('product_found', 'Product Found'), ('products-bespoke_orders', 'Products-Bespoke Orders'), ('promotion', 'Promotion'), ('search_results', 'Search Results'), ('services-service_detail', 'Services-Service Detail'), ('services-service_list', 'Services-Service List'), ('special-special_2_page', 'Special-Special 2 Page'), ('special-special_page', 'Special-Special Page'), ('terms_&_conditions', 'Terms & Conditions')], default='home', help_text='Page type, select from the available list, there can be only one instance of page for one type.', max_length=32)),
                ('page_url', models.CharField(blank=True, help_text='It has higher priority than the page type, that defines the path to the current page. Also, one page at a time may be only one page. To select the current need to enable Is current page.', max_length=255, null=True)),
                ('is_current_page', models.BooleanField(default=False, help_text='Assign this page as a current (It will display). All other pages with the same type automatically become secondary.')),
                ('title', models.CharField(help_text='Defines a title in the browser toolbar, provides a title for the page when it is added to favorites and displays a title for the page in search-engine results', max_length=64)),
                ('bespoke_orders_block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.BespokeOrdersBlock')),
                ('bespoke_screen_block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.BespokeScreenBlock')),
                ('browse_block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.BrowseBlock')),
                ('contact_block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.ContactBlock')),
                ('evaluation_kit_block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.EvaluationKitBlock')),
                ('expandable_section_block', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.ExpandableSectionBlock')),
            ],
        ),
        migrations.CreateModel(
            name='PageButton',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('title', models.CharField(help_text='Displayed text of a link (with safe template tag), If you want to modify the text style, wrap them in html tags. b - <b>Bold</b>, i - <i>Italian</i>', max_length=32)),
                ('color', models.CharField(choices=[('B', 'Blue'), ('G', 'Green'), ('W', 'White'), ('O', 'Orange')], default='W', help_text='Selection of the reserved color, that fills the background for the button. Select the color you like, border shadow and text color will change automatically.', max_length=32)),
                ('glyphicon', models.CharField(choices=[('A', 'Arrow'), ('P', 'Plus'), ('B', 'Box')], default='A', help_text='It changes the image of the glyphicon', max_length=1)),
                ('glyphicon_position', models.CharField(choices=[('L', 'Left'), ('R', 'Right')], default='R', help_text='It changes the position of the glyphicon, to display it on the left side, pick Left.', max_length=1)),
                ('external_link', models.CharField(blank=True, help_text='Fill it to add link to an external source, its priority will be higher than the internal reference.', max_length=255, null=True)),
                ('is_target_link', models.BooleanField(default=False, help_text='It enables or disables ability to open it in a new browser window or a new tab.')),
            ],
        ),
        migrations.CreateModel(
            name='PageCategoryBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('is_service_list', models.BooleanField(default=False, help_text='Display Service list')),
                ('is_detail_list', models.BooleanField(default=True, help_text='Display Category list with subcategories')),
            ],
        ),
        migrations.CreateModel(
            name='PageFooterBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('contact', models.CharField(blank=True, help_text='The name of the column with addresses, if left blank name field, contact column will not be visible in the footer.', max_length=128, null=True)),
                ('t_copy_right', models.CharField(help_text='Displayed copy right text, If you want to modify the text style, wrap them in html tags. b - <b>Bold</b>, i - <i>Italian</i>', max_length=255)),
                ('a_back_top', models.BooleanField(default=False, help_text='It enables or disables button Back to Top')),
            ],
        ),
        migrations.CreateModel(
            name='PageHeadDropMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('title', models.CharField(help_text='Displayed title of a link', max_length=64)),
                ('external_link', models.CharField(blank=True, help_text='Fill it to add link to an external source, its priority will be higher than the internal reference.', max_length=255, null=True)),
                ('priority', models.SmallIntegerField(default=1, help_text='Placing priority of the element among the same types, 1 - the first, 2 - of the second and so on.')),
                ('is_target_link', models.BooleanField(default=False, help_text='It enables or disables ability to open it in a new browser window or a new tab.')),
            ],
        ),
        migrations.CreateModel(
            name='PageHeadDropMenuElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('title', models.CharField(help_text='Displayed title of a link', max_length=64)),
                ('external_link', models.CharField(blank=True, help_text='Fill it to add link to an external source, its priority will be higher than the internal reference.', max_length=255, null=True)),
                ('priority', models.SmallIntegerField(default=1, help_text='Placing priority of the element among the same types, 1 - the first, 2 - of the second and so on.')),
                ('is_target_link', models.BooleanField(default=False, help_text='It enables or disables ability to open it in a new browser window or a new tab.')),
            ],
        ),
        migrations.CreateModel(
            name='PageHeaderBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('is_auth_menu', models.BooleanField(default=True, help_text='It enables or disables the display dependent of the authorization elements')),
                ('logo_image', models.ImageField(help_text='The recommended size of a image is 118 x 67 px. But you can use any image sizes, they will be compressed or increased to the appropriate value.', upload_to='images')),
                ('main_menus_elements', models.ManyToManyField(blank=True, to='elastic_pages.PageHeadDropMenu')),
            ],
        ),
        migrations.CreateModel(
            name='PageHeadSocLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('soc_image', models.ImageField(help_text='The recommended size of a image is 25 x 25 px. But you can use any image sizes, they will be compressed or increased to the appropriate value.', upload_to='images')),
                ('external_link', models.CharField(max_length=255)),
                ('priority', models.SmallIntegerField(default=1, help_text='Placing priority of the element among the same types, 1 - the first, 2 - of the second and so on.')),
                ('is_target_link', models.BooleanField(default=False, help_text='It enables or disables ability to open it in a new browser window or a new tab.')),
            ],
        ),
        migrations.CreateModel(
            name='PageHelpBoxBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('text', models.TextField(help_text='Displayed text of a link (with safe template tag), If you want to modify the text style, wrap them in html tags. b - <b>Bold</b>, i - <i>Italian</i>')),
                ('button', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.PageButton')),
            ],
        ),
        migrations.CreateModel(
            name='PageMainBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('background_image', models.ImageField(help_text='The recommended size of a image is 620 x 218 px. But you can use any image sizes, they will be compressed or increased to the appropriate value.', upload_to='images')),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField(help_text='Displayed text of a link (with safe template tag), If you want to modify the text style, wrap them in html tags. b - <b>Bold</b>, i - <i>Italian</i>')),
            ],
        ),
        migrations.CreateModel(
            name='PageSubCategoryBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('is_service_list', models.BooleanField(default=False, help_text='Display Service list')),
            ],
        ),
        migrations.CreateModel(
            name='PageWhatYouNeedBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('title', models.CharField(max_length=128)),
                ('left_column_title', models.CharField(max_length=64)),
                ('is_touch', models.BooleanField(default=True, help_text='It enables or disables by Touch filter')),
                ('is_colour', models.BooleanField(default=True, help_text='It enables or disables by Colour filter')),
                ('middle_column_title', models.CharField(max_length=64)),
                ('middle_column_label', models.CharField(max_length=64)),
                ('middle_column_caption', models.CharField(max_length=64)),
                ('right_column_title', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='PageWorldPayScreenBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('auto_slide', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PostsGalleryBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('title_left', models.CharField(max_length=128)),
                ('text_left', models.TextField()),
                ('image_left', models.ImageField(help_text='The recommended size of a image is 338 x 187 px. But you can use any image sizes, they will be compressed or increased to the appropriate value.', upload_to='images')),
                ('link_left', models.CharField(blank=True, max_length=255, null=True)),
                ('title_middle', models.CharField(max_length=128)),
                ('text_middle', models.TextField()),
                ('image_middle', models.ImageField(help_text='The recommended size of a image is 338 x 187 px. But you can use any image sizes, they will be compressed or increased to the appropriate value.', upload_to='images')),
                ('link_middle', models.CharField(blank=True, max_length=255, null=True)),
                ('title_right', models.CharField(max_length=128)),
                ('text_right', models.TextField()),
                ('image_right', models.ImageField(help_text='The recommended size of a image is 338 x 187 px. But you can use any image sizes, they will be compressed or increased to the appropriate value.', upload_to='images')),
                ('link_right', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetailBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
            ],
        ),
        migrations.CreateModel(
            name='SearchBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('help_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SlideElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField()),
                ('background', models.ImageField(help_text='The recommended height of image is 620px But you can use any image sizes, they will be compressed or increased to the appropriate value.', upload_to='images')),
                ('button', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.PageButton')),
            ],
        ),
        migrations.CreateModel(
            name='TextBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(help_text='Field for comments.')),
                ('title', models.TextField()),
                ('sub_title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TextElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(help_text='Field for comments.')),
                ('sub_sub_title', models.TextField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TextPhotoBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('title', models.CharField(max_length=128)),
                ('sub_title', models.CharField(max_length=128)),
                ('sub_sub_title', models.CharField(max_length=128)),
                ('top_text', models.TextField()),
                ('left_photo', models.ImageField(help_text='The recommended size of a image is 278 x 209 px. But you can use any image sizes, they will be compressed or increased to the appropriate value.', upload_to='images')),
                ('left_photo_caption', models.CharField(max_length=128)),
                ('right_text', models.TextField()),
                ('middle_text', models.TextField(blank=True, null=True)),
                ('right_photo', models.ImageField(help_text='The recommended size of a image is 278 x 209 px. But you can use any image sizes, they will be compressed or increased to the appropriate value.', upload_to='images')),
                ('right_photo_caption', models.CharField(max_length=128)),
                ('left_text', models.TextField()),
                ('bottom_text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VideoBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('title', models.CharField(max_length=128)),
                ('sub_title', models.CharField(max_length=128)),
                ('summary', models.CharField(max_length=128)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='VideoObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('sub_name', models.CharField(blank=True, max_length=128, null=True)),
                ('description', models.TextField(help_text='Field for comments.')),
                ('video', models.FileField(blank=True, null=True, upload_to='videos')),
                ('embed_video', models.TextField(blank=True, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Category')),
            ],
        ),
        migrations.CreateModel(
            name='WizardProductFoundBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(help_text='Field for comments.')),
            ],
        ),
        migrations.AddField(
            model_name='videoblock',
            name='video_obj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_obj', to='elastic_pages.VideoObject'),
        ),
        migrations.AddField(
            model_name='textblock',
            name='text_element',
            field=models.ManyToManyField(to='elastic_pages.TextElement'),
        ),
        migrations.AddField(
            model_name='pageworldpayscreenblock',
            name='slide_elem',
            field=models.ManyToManyField(to='elastic_pages.SlideElement'),
        ),
        migrations.AddField(
            model_name='pageheaderblock',
            name='soc_links',
            field=models.ManyToManyField(blank=True, to='elastic_pages.PageHeadSocLink'),
        ),
        migrations.AddField(
            model_name='pageheaddropmenu',
            name='drop_links',
            field=models.ManyToManyField(blank=True, to='elastic_pages.PageHeadDropMenuElement'),
        ),
        migrations.AddField(
            model_name='pagefooterblock',
            name='a_link',
            field=models.ManyToManyField(blank=True, to='elastic_pages.PageHeadDropMenuElement'),
        ),
        migrations.AddField(
            model_name='pagefooterblock',
            name='contact_address',
            field=models.ManyToManyField(help_text='Specify no more than 2 addresses simultaneously.', to='company.Address'),
        ),
        migrations.AddField(
            model_name='pagefooterblock',
            name='top_links',
            field=models.ManyToManyField(blank=True, to='elastic_pages.PageHeadDropMenu'),
        ),
        migrations.AddField(
            model_name='page',
            name='footer_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.PageFooterBlock'),
        ),
        migrations.AddField(
            model_name='page',
            name='get_in_touch_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.GetInTouchBlock'),
        ),
        migrations.AddField(
            model_name='page',
            name='header_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.PageHeaderBlock'),
        ),
        migrations.AddField(
            model_name='page',
            name='help_box_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.PageHelpBoxBlock'),
        ),
        migrations.AddField(
            model_name='page',
            name='latest_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.LatestBlock'),
        ),
        migrations.AddField(
            model_name='page',
            name='main_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.PageMainBlock'),
        ),
        migrations.AddField(
            model_name='page',
            name='news_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.NewsBlock'),
        ),
        migrations.AddField(
            model_name='page',
            name='our_people_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.OurPeopleBlock'),
        ),
        migrations.AddField(
            model_name='page',
            name='posts_gallery_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.PostsGalleryBlock'),
        ),
        migrations.AddField(
            model_name='page',
            name='product_category_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.PageCategoryBlock'),
        ),
        migrations.AddField(
            model_name='page',
            name='product_detail_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.ProductDetailBlock'),
        ),
        migrations.AddField(
            model_name='page',
            name='product_subcategory_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.PageSubCategoryBlock'),
        ),
        migrations.AddField(
            model_name='page',
            name='search_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.SearchBlock'),
        ),
        migrations.AddField(
            model_name='page',
            name='text_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.TextBlock'),
        ),
        migrations.AddField(
            model_name='page',
            name='text_photo_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.TextPhotoBlock'),
        ),
        migrations.AddField(
            model_name='page',
            name='video_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.VideoBlock'),
        ),
        migrations.AddField(
            model_name='page',
            name='what_you_need_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.PageWhatYouNeedBlock'),
        ),
        migrations.AddField(
            model_name='page',
            name='wizard_product_found_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.WizardProductFoundBlock'),
        ),
        migrations.AddField(
            model_name='page',
            name='worldpay_slide_block',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.PageWorldPayScreenBlock'),
        ),
        migrations.AddField(
            model_name='latestblock',
            name='video_main',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_main', to='elastic_pages.VideoObject'),
        ),
        migrations.AddField(
            model_name='latestblock',
            name='video_second',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_second', to='elastic_pages.VideoObject'),
        ),
        migrations.AddField(
            model_name='latestblock',
            name='video_third',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_third', to='elastic_pages.VideoObject'),
        ),
        migrations.AddField(
            model_name='bespokescreenblock',
            name='button',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='elastic_pages.PageButton'),
        ),
    ]
