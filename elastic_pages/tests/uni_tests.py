"""Module Elastic Pages function unittest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import os

import tempfile
from django.apps import apps

from django.core.urlresolvers import reverse
from django.test import TestCase

from address.models import Address
from elastic_pages.models import Page, PageHeaderBlock, PageHeadDropMenu,\
    PageHeadDropMenuElement, PageHeadSocLink, PageButton, PageHelpBoxBlock, \
    PageMainBlock, PageFooterBlock, PageWhatYouNeedBlock



__all__ = ['PageModelsTestCase']


_external_link = 'http://www.websitetest.com/'

_page_data = {
    'name': 'Test Main Page',
    'description': 'Test Main Page Description',
    'page_type': 'home',
    'title': 'Test | Main Page',
}

_header_data = {
    'name': 'Test Header',
    'description': 'Test Header Description',
    'is_auth_menu': False,
    'logo_image': tempfile.NamedTemporaryFile(suffix=".jpg").name
}

_head_link_data = {
    'name': 'Test Link',
    'title': 'Test Link Title',
}

_head_drop_link_data = {
    'name': 'Test Drop Link',
    'title': 'Test Drop Link Title',
}

_head_soc_link_data = {
    'name': 'Test Drop Link',
    'soc_image': tempfile.NamedTemporaryFile(suffix=".jpg").name,
    'external_link': _external_link
}

_help_box_data = {
    'name': 'Test Help Box',
    'description': 'Test Help Box Description',
    'text': 'Test <b>text</b>',
}

_button_data = {
    'name': 'Test Name',
    'title': 'Test Button',
    'color': 'White',
    'glyphicon': 'Arrow',
    'glyphicon_position': 'Right',
    'internal_link': 'home',
}

_main_block_data = {
    'name': 'Test Name',
    'description': 'Test Main Description',
    'title': 'Test Main Block',
    'background_image': tempfile.NamedTemporaryFile(suffix=".jpg").name,
    'text': 'Test <a href="/">text</a>'
}

_footer_block_data = {
    'name': 'Test name',
    'description': 'Test description',
    'contact': 'Contact test',
    't_copy_right': 'Test copyright',
    'a_back_top': False
}

_address_block = {
    'name': 'Test name',
    'description': 'Test description',
    'title': 'Test title',
    'line_1': 'Test line 1',
    'line_2': 'Test line 2',
    'phone': '+1 (2)345-678-901'
}

_whatyouneed_block_data = {
    'name': 'Test name',
    'description': 'Test description',
    'title': 'Test title',
    'left_column_title': 'Test L Title',
    'is_touch': True,
    'is_colour': True,
    'middle_column_title': 'Test M Title',
    'middle_column_label': 'Test M label',
    'middle_column_caption': 'Test M caption',
    'right_column_title': 'Test R Title'
}


class PageModelsTestCase(TestCase):

    def test_create_page(self):
        """Test ability to create a empty page"""
        self.assertEqual(self.client.get(reverse('home')).status_code, 404)

        page = Page.objects.create(**_page_data)

        self.assertEqual(page.title, _page_data['title'])
        self.assertEqual(page.page_type, _page_data['page_type'])

        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertIn('page_settings', response.context_data)

    def test_create_page_with_header(self):
        """Test ability to create a page with full header"""

        link_1 = PageHeadDropMenu.objects.create\
            (internal_link='home', **_head_link_data)
        link_2 = PageHeadDropMenu.objects.create(
            external_link=_external_link, **_head_link_data)
        link_3 = PageHeadDropMenu.objects.create(**_head_link_data)
        link_element_1 = PageHeadDropMenuElement.objects.create(
            internal_link='home', **_head_drop_link_data)
        link_element_2 = PageHeadDropMenuElement.objects.create(
            external_link=_external_link, **_head_drop_link_data)
        link_3.drop_links.add(link_element_1, link_element_2)

        soc_link = PageHeadSocLink.objects.create(**_head_soc_link_data)

        header = PageHeaderBlock.objects.create(**_header_data)
        header.main_menus_elements.add(link_1, link_2, link_3)
        header.soc_links.add(soc_link)

        page = Page.objects.create(header_block=header, **_page_data)

        self.assertEqual(page.header_block, header)
        self.assertEqual(page.header_block.main_menus_elements.count(), 3)
        self.assertEqual(link_3.drop_links.count(), 2)

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

        self.assertIn('logo', response.context)
        self.assertTrue(response.context['logo'].endswith('.jpg'))

        self.assertIn('auth_menu', response.context)
        self.assertFalse(response.context['auth_menu'])

        self.assertIn('soc_links', response.context)
        self.assertIn(soc_link, response.context['soc_links'])

        self.assertIn('d_d_menu', response.context)
        self.assertIn(link_2, response.context['d_d_menu'])

    def test_create_page_with_help_box(self):
        """Test ability to create a page with help box"""

        button = PageButton.objects.create(**_button_data)
        help_block = PageHelpBoxBlock.objects.create(
            button=button, **_help_box_data)
        page = Page.objects.create(help_box_block=help_block, **_page_data)

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

        self.assertEqual(page.help_box_block.button, button)
        self.assertIn('text', response.context)
        self.assertIn('button', response.context)

    def test_create_page_with_main_box(self):
        """Test ability to create a page with main box"""

        main_block = PageMainBlock.objects.create(**_main_block_data)
        Page.objects.create(main_block=main_block, **_page_data)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

        self.assertIn('text', response.context)
        self.assertIn('title', response.context)
        self.assertIn('image', response.context)

    def test_create_page_with_footer(self):
        """Test ability to create a page with main footer"""

        footer_block = PageFooterBlock.objects.create(**_footer_block_data)
        link_1 = PageHeadDropMenu.objects.create\
            (internal_link='home', **_head_link_data)
        link_2 = PageHeadDropMenu.objects.create(
            external_link=_external_link, **_head_link_data)
        link_3 = PageHeadDropMenu.objects.create(**_head_link_data)
        link_element_1 = PageHeadDropMenuElement.objects.create(
            internal_link='home', **_head_drop_link_data)
        link_element_2 = PageHeadDropMenuElement.objects.create(
            external_link=_external_link, **_head_drop_link_data)
        link_3.drop_links.add(link_element_1, link_element_2)
        footer_block.top_links.add(link_1, link_2, link_3)
        contact_address = Address.objects.create(**_address_block)
        footer_block.contact_address.add(contact_address)
        footer_block.a_link.add(link_element_1)

        Page.objects.create(footer_block=footer_block, **_page_data)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

        self.assertIn('top_links', response.context)
        self.assertIn('contact', response.context)
        self.assertIn('top_contacts', response.context)
        self.assertIn('bot_copy_right', response.context)
        self.assertIn('bot_link', response.context)
        self.assertIn('bot_back_top', response.context)

    def test_create_page_with_whatyouneed_block(self):
        """Test ability to create a page with main what you need block"""

        what_you_need_block = PageWhatYouNeedBlock.objects.create(
            **_whatyouneed_block_data)
        Page.objects.create(what_you_need_block=what_you_need_block,
                            **_page_data)

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

        self.assertIn('title', response.context)
        self.assertIn('left_column_title', response.context)
        self.assertIn('is_touch', response.context)
        self.assertIn('is_colour', response.context)
        self.assertIn('middle_column_title', response.context)
        self.assertIn('middle_column_label', response.context)
        self.assertIn('middle_column_caption', response.context)
        self.assertIn('right_column_title', response.context)

    def test_migration(self):
        pass
