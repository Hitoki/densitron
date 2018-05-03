# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-15 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elastic_pages', '0002_auto_20160316_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='page_type',
            field=models.CharField(choices=[('company-about_us', 'Company-About Us'), ('company-career_opportunities', 'Company-Career Opportunities'), ('company-company_detail', 'Company-Company Detail'), ('company-news', 'Company-News'), ('company-news_detail', 'Company-News Detail'), ('company-our_people', 'Company-Our People'), ('contact', 'Contact'), ('home', 'Home'), ('knowledge-base', 'Knowledge-Base'), ('privacy', 'Privacy'), ('product-product_detail', 'Product-Product Detail'), ('product-product_detail_kit', 'Product-Product Detail Kit'), ('product-technology', 'Product-Technology'), ('product-technology_detail', 'Product-Technology Detail'), ('product_found', 'Product Found'), ('products-bespoke_orders', 'Products-Bespoke Orders'), ('promotion', 'Promotion'), ('search_results', 'Search Results'), ('services-service_detail', 'Services-Service Detail'), ('services-service_list', 'Services-Service List'), ('special-special_2_page', 'Special-Special 2 Page'), ('special-special_page', 'Special-Special Page'), ('terms_&_conditions', 'Terms & Conditions')], default='home', help_text='Page type, select from the available list, there can be only one instance of page for one type.', max_length=32),
        ),
    ]
