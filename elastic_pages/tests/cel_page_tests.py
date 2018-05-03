"""Module Elastic Pages Selenium unittest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import os
import time

from os.path import join

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from selenium import webdriver

from address.models import Address
from elastic_pages.models import PageHeadSocLink, PageHeadDropMenu, \
    PageHeadDropMenuElement, PageHeaderBlock, Page, PageButton, \
    PageHelpBoxBlock, PageMainBlock, PageFooterBlock, PageWhatYouNeedBlock
from elastic_pages.snippets import get_header_menu_architect


_external_link = 'http://densitron.anvil8.com/'

_page_data = {
    'name': 'Page Not Found Test Name',
    'description': 'Page Not Found Test Description',
    'page_type': 'page_not_found',
    'title': 'Page Not Found Test Title',
}

_header_data = {
    'name': 'PNF Test Header Name',
    'description': 'PNF Test Header Description',
    'logo_image': join(os.getcwd(), "static/test_images/logo-v2.jpeg")
}

_head_soc_link_data = {
    'external_link': _external_link
}

_head_drop_link_data = {
    'name': 'PNF Test Link',
    'title': 'Test Drop Link Title',
}

_head_link_data = {
    'name': 'Test Link',
    'title': 'Test Link Title',
}

_help_box_data = {
    'name': 'Test Help Box',
    'description': 'Test Help Box Description',
    'text': '<span>Densitron Technologles</span> is a world leading designer '
            'and manufacturer of information display system.',
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
    'text': "We're sorry, The page you were looking for cannot be found.<br> "
            "View our <a href=''>Products</a> or <a href=''>Services</a> "
            "or return to the <a href=''>Home Page.</a></p>"
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


class MySeleniumTests(StaticLiveServerTestCase):

    def setUp(self):

        self.selenium = webdriver.Firefox()
        # self.selenium.maximize_window()
        super(MySeleniumTests, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(MySeleniumTests, self).tearDown()

    def admin_login(self):
        self.selenium.get(
            '{}{}'.format(self.live_server_url, "/admin/")
        )

        username = self.selenium.find_element_by_id("id_username")
        username.send_keys("anvil8")
        password = self.selenium.find_element_by_id("id_password")
        password.send_keys("densitron")
        self.selenium.find_element_by_xpath('//input[@value="Log in"]')\
            .click()

    def test_admin_login_logout(self):
        """
        Django admin login superuser test
        """
        self.admin_login()

        self.selenium.get('{}{}'.format(self.live_server_url, "/admin/"))

        self.assertIn("Site administration | Django site admin",
                      self.selenium.title)

        self.selenium.find_element_by_xpath('//*[@id="user-tools"]/a[3]')\
            .click()

        self.assertIn("Logged out | Django site admin", self.selenium.title)

    def test_create_header_for_404_page(self):
        """Create full header on 404 page"""
        # Create admin, if he is not exist
        if not User.objects.filter(is_staff=True):
            User.objects.create_superuser(
                'anvil8', 'anvil8@anvil8.com', 'densitron')

        # Login admin
        self.admin_login()

        # Click Add new Page
        self.selenium.find_element_by_css_selector('tr.model-page a.addlink')\
            .click()
        self.assertIn('Add page | Django site admin', self.selenium.title)

        # Fill the page data fields
        self.selenium.find_element_by_id('id_name')\
            .send_keys(_page_data['name'])
        self.selenium.find_element_by_id('id_description')\
            .send_keys(_page_data['description'])
        self.selenium.find_element_by_id('id_page_type')\
            .send_keys(_page_data['page_type'])
        self.selenium.find_element_by_id('id_title')\
            .send_keys(_page_data['title'])

        # Create main window handle
        main_window = self.selenium.window_handles[0]

        # # Go to create header block page
        self.selenium.find_element_by_id('add_id_header_block').click()
        self.selenium.implicitly_wait(3)

        # Create header window handle
        header_window = self.selenium.window_handles[-1]

        # Switch to header handle
        self.selenium.switch_to.window(header_window)

        # Fill the header data fields
        self.selenium.find_element_by_id('id_name')\
            .send_keys(_header_data['name'])
        self.selenium.find_element_by_id('id_description')\
            .send_keys(_header_data['description'])
        self.selenium.find_element_by_id('id_logo_image')\
            .send_keys(_header_data['logo_image'])

        # Go to add social links create page
        self.selenium.find_element_by_id('add_id_soc_links').click()

        # Create link window handle
        link_window = self.selenium.window_handles[-1]

        # Switch to link handle
        self.selenium.switch_to.window(link_window)

        # # # Create soc link 1

        # Fill the social link data
        self.selenium.find_element_by_id('id_name')\
            .send_keys('PNF Test Header Twitter Soc Link')
        self.selenium.find_element_by_id('id_soc_image').clear()
        self.selenium.find_element_by_id('id_soc_image')\
            .send_keys(join(os.getcwd(), 'static/test_images/twitter.jpeg'))
        self.selenium.find_element_by_id('id_external_link')\
            .send_keys(_head_soc_link_data['external_link'])
        self.selenium.find_element_by_id('id_is_target_link').click()
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Switch to header page
        self.selenium.switch_to.window(header_window)

        # Go to add social links create page
        self.selenium.find_element_by_id('add_id_soc_links').click()
        self.selenium.implicitly_wait(3)

        # # # Create soc link 2

        # Create link window handle
        link_window = self.selenium.window_handles[-1]

        # Switch to link handle
        self.selenium.switch_to.window(link_window)

        # Fill the social link data
        self.selenium.find_element_by_id('id_name')\
            .send_keys('PNF Test Header LinkedIn Soc Link')
        self.selenium.find_element_by_id('id_soc_image').clear()
        self.selenium.find_element_by_id('id_soc_image')\
            .send_keys(join(os.getcwd(), 'static/test_images/linkedin.jpeg'))
        self.selenium.find_element_by_id('id_external_link')\
            .send_keys(_head_soc_link_data['external_link'])
        self.selenium.find_element_by_id('id_is_target_link').click()
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Switch to header page
        self.selenium.switch_to.window(header_window)

        # Go to add social links create page
        self.selenium.find_element_by_id('add_id_soc_links').click()
        self.selenium.implicitly_wait(3)

        # # # Create soc link 3

        # Create link window handle
        link_window = self.selenium.window_handles[-1]

        # Switch to link handle
        self.selenium.switch_to.window(link_window)

        # Fill the social link data
        self.selenium.find_element_by_id('id_name')\
            .send_keys('PNF Test Header ShareThis Soc Link')
        self.selenium.find_element_by_id('id_soc_image').clear()
        self.selenium.find_element_by_id('id_soc_image')\
            .send_keys(join(os.getcwd(), 'static/test_images/sharethis.jpeg'))
        self.selenium.find_element_by_id('id_external_link')\
            .send_keys(_head_soc_link_data['external_link'])
        self.selenium.find_element_by_id('id_is_target_link').click()
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Switch to header page
        self.selenium.switch_to.window(header_window)

        _header_menu_architect = get_header_menu_architect()

        for key, values in _header_menu_architect.items():
            # Go to add main menu elements page
            self.selenium.find_element_by_id('add_id_main_menus_elements')\
                .click()
            self.selenium.implicitly_wait(3)

            # Create menu window handle
            menu_window = self.selenium.window_handles[-1]

            # Switch to menu handle
            self.selenium.switch_to.window(menu_window)

            # # # Create menu element
            self.selenium.find_element_by_id('id_name')\
                .send_keys(key.title())
            self.selenium.find_element_by_id('id_title')\
                .send_keys(key.title())

            if isinstance(values, str):
                self.selenium.find_element_by_id('id_internal_link')\
                    .send_keys(key)
            else:
                for value in values:
                    self.selenium.find_element_by_id('add_id_drop_links')\
                        .click()
                    # Create menu drop list handle
                    drop_list_window = self.selenium.window_handles[-1]

                    # Switch to drop list handle
                    self.selenium.switch_to.window(drop_list_window)

                    self.selenium.find_element_by_id('id_name')\
                        .send_keys(' '.join(value.title().split('_')))
                    self.selenium.find_element_by_id('id_title')\
                        .send_keys(' '.join(value.title().split('_')))
                    self.selenium.find_element_by_id('id_is_target_link')\
                        .click()
                    self.selenium.find_element_by_id('id_internal_link')\
                        .send_keys(join(key, '-', value))
                    self.selenium.find_element_by_xpath(
                        '//input[@value="Save"]').click()

                    # Switch to menu handle
                    self.selenium.switch_to.window(menu_window)
            self.selenium.find_element_by_xpath('//input[@value="Save"]')\
                .click()

            # Switch to header page
            self.selenium.switch_to.window(header_window)

        # Save Header page changes
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Switch to main page
        self.selenium.switch_to.window(main_window)

        # Save and fill last main page data
        self.selenium.find_element_by_id('id_header_block').send_keys(1)
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Get Page Not Found Page
        self.selenium.get('{}{}'.format(
            self.live_server_url, "/page_not_found"))

        # Sleep 5 sec (For clarity, the correct display of the result)
        time.sleep(5)

    def test_create_help_box_for_404_page(self):
        """Create full help box on 404 page"""
        # Create admin, if he is not exist
        if not User.objects.filter(is_staff=True):
            User.objects.create_superuser(
                'anvil8', 'anvil8@anvil8.com', 'densitron')

        # Login admin
        self.admin_login()

        # Click Add new Page
        self.selenium.find_element_by_css_selector('tr.model-page a.addlink')\
            .click()
        self.assertIn('Add page | Django site admin', self.selenium.title)

        # Fill the page data fields
        self.selenium.find_element_by_id('id_name')\
            .send_keys(_page_data['name'])
        self.selenium.find_element_by_id('id_description')\
            .send_keys(_page_data['description'])
        self.selenium.find_element_by_id('id_page_type')\
            .send_keys(_page_data['page_type'])
        self.selenium.find_element_by_id('id_title')\
            .send_keys(_page_data['title'])

        # Create main window handle
        main_window = self.selenium.window_handles[0]

        # # Go to create help block page
        self.selenium.find_element_by_id('add_id_help_box_block').click()
        self.selenium.implicitly_wait(3)

        # Create help window handle
        help_window = self.selenium.window_handles[-1]

        # Switch to help handle
        self.selenium.switch_to.window(help_window)

        # Fill the help data fields
        self.selenium.find_element_by_id('id_name')\
            .send_keys(_help_box_data['name'])
        self.selenium.find_element_by_id('id_description')\
            .send_keys(_help_box_data['description'])
        self.selenium.find_element_by_id('id_text')\
            .send_keys(_help_box_data['text'])
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Switch to main page
        self.selenium.switch_to.window(main_window)

        # Save and fill last main page data
        self.selenium.find_element_by_id('id_help_box_block').send_keys(1)
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Get Page Not Found Page
        self.selenium.get('{}{}'.format(
            self.live_server_url, "/page_not_found"))

        # Sleep 5 sec (For clarity, the correct display of the result)
        time.sleep(5)

    def test_create_help_box_with_button_for_404_page(self):
        """Create full help box on 404 page"""
        # Create admin, if he is not exist
        if not User.objects.filter(is_staff=True):
            User.objects.create_superuser(
                'anvil8', 'anvil8@anvil8.com', 'densitron')

        # Login admin
        self.admin_login()

        # Click Add new Page
        self.selenium.find_element_by_css_selector('tr.model-page a.addlink')\
            .click()
        self.assertIn('Add page | Django site admin', self.selenium.title)

        # Fill the page data fields
        self.selenium.find_element_by_id('id_name')\
            .send_keys(_page_data['name'])
        self.selenium.find_element_by_id('id_description')\
            .send_keys(_page_data['description'])
        self.selenium.find_element_by_id('id_page_type')\
            .send_keys(_page_data['page_type'])
        self.selenium.find_element_by_id('id_title')\
            .send_keys(_page_data['title'])

        # Create main window handle
        main_window = self.selenium.window_handles[0]

        # # Go to create help block page
        self.selenium.find_element_by_id('add_id_help_box_block').click()
        self.selenium.implicitly_wait(3)

        # Create help window handle
        help_window = self.selenium.window_handles[-1]

        # Switch to help handle
        self.selenium.switch_to.window(help_window)

        # Fill the help data fields
        self.selenium.find_element_by_id('id_name')\
            .send_keys(_help_box_data['name'])
        self.selenium.find_element_by_id('id_description')\
            .send_keys(_help_box_data['description'])
        self.selenium.find_element_by_id('id_text')\
            .send_keys(_help_box_data['text'])

        # Go to create button page
        self.selenium.find_element_by_id('add_id_button').click()

        # Create button window handle
        button_window = self.selenium.window_handles[-1]

        # Switch to button handle
        self.selenium.switch_to.window(button_window)

        # Fill the button data fields
        self.selenium.find_element_by_id('id_name')\
            .send_keys(_button_data['name'])
        self.selenium.find_element_by_id('id_title')\
            .send_keys(_button_data['title'])
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Switch to help page
        self.selenium.switch_to.window(help_window)

        # Save last help box data
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Switch to main page
        self.selenium.switch_to.window(main_window)

        # Save and fill last main page data
        self.selenium.find_element_by_id('id_help_box_block').send_keys(1)
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Get Page Not Found Page
        self.selenium.get('{}{}'.format(
            self.live_server_url, "/page_not_found"))

        # Sleep 5 sec (For clarity, the correct display of the result)
        time.sleep(5)

    def test_create_main_box_for_404_page(self):
        """Create full main box on 404 page"""
        # Create admin, if he is not exist
        if not User.objects.filter(is_staff=True):
            User.objects.create_superuser(
                'anvil8', 'anvil8@anvil8.com', 'densitron')

        # Login admin
        self.admin_login()

        # Click Add new Page
        self.selenium.find_element_by_css_selector('tr.model-page a.addlink')\
            .click()
        self.assertIn('Add page | Django site admin', self.selenium.title)

        # Fill the page data fields
        self.selenium.find_element_by_id('id_name')\
            .send_keys(_page_data['name'])
        self.selenium.find_element_by_id('id_description')\
            .send_keys(_page_data['description'])
        self.selenium.find_element_by_id('id_page_type')\
            .send_keys(_page_data['page_type'])
        self.selenium.find_element_by_id('id_title')\
            .send_keys(_page_data['title'])

        # Create main window handle
        main_window = self.selenium.window_handles[0]

        # # Go to create main block page
        self.selenium.find_element_by_id('add_id_main_block').click()
        self.selenium.implicitly_wait(3)

        # Create main_box window handle
        main_box_window = self.selenium.window_handles[-1]

        # Switch to main_box handle
        self.selenium.switch_to.window(main_box_window)

        # Fill the main_box data fields
        self.selenium.find_element_by_id('id_name')\
            .send_keys(_main_block_data['name'])
        self.selenium.find_element_by_id('id_description')\
            .send_keys(_main_block_data['description'])
        self.selenium.find_element_by_id('id_title')\
            .send_keys(_main_block_data['title'])
        self.selenium.find_element_by_id('id_text')\
            .send_keys(_main_block_data['text'])
        self.selenium.find_element_by_id('id_background_image')\
            .send_keys(join(
                os.getcwd(), 'static/test_images/densitron-image.jpeg'))
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Switch to main page
        self.selenium.switch_to.window(main_window)

        # Save and fill last main page data
        self.selenium.find_element_by_id('id_main_block').send_keys(1)
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Get Page Not Found Page
        self.selenium.get('{}{}'.format(
            self.live_server_url, "/page_not_found"))

        # Sleep 5 sec (For clarity, the correct display of the result)
        time.sleep(5)

    def test_create_footer_for_404_page(self):
        """Create full footer box on 404 page"""
        # Create admin, if he is not exist
        if not User.objects.filter(is_staff=True):
            User.objects.create_superuser(
                'anvil8', 'anvil8@anvil8.com', 'densitron')

        # Login admin
        self.admin_login()

        # Click Add new Page
        self.selenium.find_element_by_css_selector('tr.model-page a.addlink')\
            .click()
        self.assertIn('Add page | Django site admin', self.selenium.title)

        # Fill the page data fields
        self.selenium.find_element_by_id('id_name')\
            .send_keys(_page_data['name'])
        self.selenium.find_element_by_id('id_description')\
            .send_keys(_page_data['description'])
        self.selenium.find_element_by_id('id_page_type')\
            .send_keys(_page_data['page_type'])
        self.selenium.find_element_by_id('id_title')\
            .send_keys(_page_data['title'])

        # Create main window handle
        main_window = self.selenium.window_handles[0]

        # # Go to create footer block page
        self.selenium.find_element_by_id('add_id_footer_block').click()
        self.selenium.implicitly_wait(3)

        # Create footer window handle
        footer_window = self.selenium.window_handles[-1]

        # Switch to footer handle
        self.selenium.switch_to.window(footer_window)

        # Fill the footer fields
        self.selenium.find_element_by_id('id_name')\
            .send_keys(_footer_block_data['name'])
        self.selenium.find_element_by_id('id_description')\
            .send_keys(_footer_block_data['description'])
        self.selenium.find_element_by_id('id_a_back_top').click()
        self.selenium.find_element_by_id('id_contact')\
            .send_keys(_footer_block_data['contact'])
        self.selenium.find_element_by_id('id_t_copy_right')\
            .send_keys(_footer_block_data['t_copy_right'])

        # Go to create bot link page
        self.selenium.find_element_by_id('add_id_a_link').click()

        # # # Create bot link window handle
        b_link_window = self.selenium.window_handles[-1]

        # Switch to bot link handle
        self.selenium.switch_to.window(b_link_window)

        # Fill the bot link fields
        self.selenium.find_element_by_id('id_name')\
            .send_keys(_head_link_data['name'])
        self.selenium.find_element_by_id('id_title')\
            .send_keys(_head_link_data['title'])
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Switch to footer handle
        self.selenium.switch_to.window(footer_window)

        # # # Go to create bot link 2 page
        self.selenium.find_element_by_id('add_id_a_link').click()

        # Create bot link window handle
        b_link_window = self.selenium.window_handles[-1]

        # Switch to bot link handle
        self.selenium.switch_to.window(b_link_window)

        # Fill the bot link fields
        self.selenium.find_element_by_id('id_name')\
            .send_keys(_head_link_data['name'])
        self.selenium.find_element_by_id('id_title')\
            .send_keys(_head_link_data['title'])
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Switch to footer handle
        self.selenium.switch_to.window(footer_window)

        # Go to create address page
        self.selenium.find_element_by_id('add_id_contact_address').click()

        # Create address window handle
        address_window = self.selenium.window_handles[-1]

        # Switch to address handle
        self.selenium.switch_to.window(address_window)

        # Fill the address fields
        self.selenium.find_element_by_id('id_name')\
            .send_keys(_address_block['name'])
        self.selenium.find_element_by_id('id_description')\
            .send_keys(_address_block['description'])
        self.selenium.find_element_by_id('id_title')\
            .send_keys(_address_block['title'])
        self.selenium.find_element_by_id('id_line_1')\
            .send_keys(_address_block['line_1'])
        self.selenium.find_element_by_id('id_line_2')\
            .send_keys(_address_block['line_2'])
        self.selenium.find_element_by_id('id_phone')\
            .send_keys(_address_block['phone'])
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Switch to footer handle
        self.selenium.switch_to.window(footer_window)

        # Go to create address page
        self.selenium.find_element_by_id('add_id_contact_address').click()

        # Create address window handle
        address_window = self.selenium.window_handles[-1]

        # Switch to address handle
        self.selenium.switch_to.window(address_window)

        # Fill the address 2 fields
        self.selenium.find_element_by_id('id_name')\
            .send_keys(_address_block['name'])
        self.selenium.find_element_by_id('id_description')\
            .send_keys(_address_block['description'])
        self.selenium.find_element_by_id('id_title')\
            .send_keys(_address_block['title'])
        self.selenium.find_element_by_id('id_line_1')\
            .send_keys(_address_block['line_1'])
        self.selenium.find_element_by_id('id_line_2')\
            .send_keys(_address_block['line_2'])
        self.selenium.find_element_by_id('id_phone')\
            .send_keys(_address_block['phone'])
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Switch to footer handle
        self.selenium.switch_to.window(footer_window)

        _footer_menu_architect = get_header_menu_architect()

        for key, values in _footer_menu_architect.items():
            # Go to add main menu elements page
            self.selenium.find_element_by_id('add_id_top_links')\
                .click()
            self.selenium.implicitly_wait(3)

            # Create menu window handle
            menu_window = self.selenium.window_handles[-1]

            # Switch to menu handle
            self.selenium.switch_to.window(menu_window)

            # # # Create menu element
            self.selenium.find_element_by_id('id_name')\
                .send_keys(key.title())
            self.selenium.find_element_by_id('id_title')\
                .send_keys(key.title())

            if isinstance(values, str):
                self.selenium.find_element_by_id('id_internal_link')\
                    .send_keys(key)
            else:
                for value in values:
                    self.selenium.find_element_by_id('add_id_drop_links')\
                        .click()
                    # Create menu drop list handle
                    drop_list_window = self.selenium.window_handles[-1]

                    # Switch to drop list handle
                    self.selenium.switch_to.window(drop_list_window)

                    self.selenium.find_element_by_id('id_name')\
                        .send_keys(' '.join(value.title().split('_')))
                    self.selenium.find_element_by_id('id_title')\
                        .send_keys(' '.join(value.title().split('_')))
                    self.selenium.find_element_by_id('id_is_target_link')\
                        .click()
                    self.selenium.find_element_by_id('id_internal_link')\
                        .send_keys(join(key, '-', value))
                    self.selenium.find_element_by_xpath(
                        '//input[@value="Save"]').click()

                    # Switch to menu handle
                    self.selenium.switch_to.window(menu_window)
            self.selenium.find_element_by_xpath('//input[@value="Save"]')\
                .click()

            # Switch to footer page
            self.selenium.switch_to.window(footer_window)

        # Save footer last data
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Switch to main page
        self.selenium.switch_to.window(main_window)

        # Save and fill last main page data
        self.selenium.find_element_by_id('id_footer_block').send_keys(1)
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Get Page Not Found Page
        self.selenium.get('{}{}'.format(
            self.live_server_url, "/page_not_found"))

        # Sleep 5 sec (For clarity, the correct display of the result)
        time.sleep(5)

    def test_create_whatyouneed_for_404_page(self):
        """Create full what you need box on 404 page"""
        # Create admin, if he is not exist
        if not User.objects.filter(is_staff=True):
            User.objects.create_superuser(
                'anvil8', 'anvil8@anvil8.com', 'densitron')

        # Login admin
        self.admin_login()

        # Click Add new Page
        self.selenium.find_element_by_css_selector('tr.model-page a.addlink')\
            .click()
        self.assertIn('Add page | Django site admin', self.selenium.title)

        # Fill the page data fields
        self.selenium.find_element_by_id('id_name')\
            .send_keys(_page_data['name'])
        self.selenium.find_element_by_id('id_description')\
            .send_keys(_page_data['description'])
        self.selenium.find_element_by_id('id_page_type')\
            .send_keys(_page_data['page_type'])
        self.selenium.find_element_by_id('id_title')\
            .send_keys(_page_data['title'])

        # Create main window handle
        main_window = self.selenium.window_handles[0]

        # # Go to create what_you_need block page
        self.selenium.find_element_by_id('add_id_what_you_need_block').click()
        self.selenium.implicitly_wait(3)

        # Create what_you_need window handle
        what_you_need_window = self.selenium.window_handles[-1]

        # Switch to what_you_need handle
        self.selenium.switch_to.window(what_you_need_window)

        # Fill the what_you_need data fields
        self.selenium.find_element_by_id('id_name')\
            .send_keys(_whatyouneed_block_data['name'])
        self.selenium.find_element_by_id('id_description')\
            .send_keys(_whatyouneed_block_data['description'])
        self.selenium.find_element_by_id('id_title')\
            .send_keys(_whatyouneed_block_data['title'])
        self.selenium.find_element_by_id('id_left_column_title')\
            .send_keys(_whatyouneed_block_data['left_column_title'])
        self.selenium.find_element_by_id('id_middle_column_label')\
            .send_keys(_whatyouneed_block_data['middle_column_label'])
        self.selenium.find_element_by_id('id_middle_column_title')\
            .send_keys(_whatyouneed_block_data['middle_column_title'])
        self.selenium.find_element_by_id('id_middle_column_caption')\
            .send_keys(_whatyouneed_block_data['middle_column_caption'])
        self.selenium.find_element_by_id('id_right_column_title')\
            .send_keys(_whatyouneed_block_data['right_column_title'])
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Switch to main page
        self.selenium.switch_to.window(main_window)

        # Save and fill last main page data
        self.selenium.find_element_by_id('id_what_you_need_block')\
            .send_keys(1)
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Get Page Not Found Page
        self.selenium.get('{}{}'.format(
            self.live_server_url, "/page_not_found"))

        # Sleep 5 sec (For clarity, the correct display of the result)
        time.sleep(5)

    def assembly_404_full_page(self):
        """Create all object and assebly them to the 404 page"""
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

        soc_link = PageHeadSocLink.objects.create(
            soc_image=join(os.getcwd(), 'static/test_images/twitter.jpeg'),
            **_head_soc_link_data)
        soc_link2 = PageHeadSocLink.objects.create(
            soc_image=join(os.getcwd(), 'static/test_images/sharethis.jpeg'),
            **_head_soc_link_data)
        soc_link3 = PageHeadSocLink.objects.create(
            soc_image=join(os.getcwd(), 'static/test_images/linkedin.jpeg'),
            **_head_soc_link_data)
        header = PageHeaderBlock.objects.create(**_header_data)
        header.main_menus_elements.add(link_1, link_2, link_3)
        header.soc_links.add(soc_link, soc_link2, soc_link3)
        PageHelpBoxBlock.objects.create(**_help_box_data)
        PageMainBlock.objects.create(
            background_image=join(
                os.getcwd(), 'static/test_images/densitron-image.jpeg'),
            **_main_block_data)
        footer_block = PageFooterBlock.objects.create(**_footer_block_data)
        footer_block.top_links.add(link_1, link_2, link_3)
        contact_address = Address.objects.create(**_address_block)
        footer_block.contact_address.add(contact_address)
        footer_block.a_link.add(link_element_1)

        # Create admin, if he is not exist
        if not User.objects.filter(is_staff=True):
            User.objects.create_superuser(
                'anvil8', 'anvil8@anvil8.com', 'densitron')

        # Login admin
        self.admin_login()

        # Click Add new Page
        self.selenium.find_element_by_css_selector('tr.model-page a.addlink')\
            .click()
        self.assertIn('Add page | Django site admin', self.selenium.title)

        # Fill the page data fields
        self.selenium.find_element_by_id('id_name')\
            .send_keys(_page_data['name'])
        self.selenium.find_element_by_id('id_description')\
            .send_keys(_page_data['description'])
        self.selenium.find_element_by_id('id_page_type')\
            .send_keys(_page_data['page_type'])
        self.selenium.find_element_by_id('id_title')\
            .send_keys(_page_data['title'])
        self.selenium.find_element_by_xpath(
            '//*[@id="id_header_block"]/option[2]').click()
        self.selenium.find_element_by_xpath(
            '//*[@id="id_main_block"]/option[2]').click()
        self.selenium.find_element_by_xpath(
            '//*[@id="id_help_box_block"]/option[2]').click()
        self.selenium.find_element_by_xpath(
            '//*[@id="id_footer_block"]/option[2]').click()
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Get Page Not Found Page
        self.selenium.get('{}{}'.format(
            self.live_server_url, "/page_not_found"))

        # Sleep 5 sec (For clarity, the correct display of the result)
        time.sleep(5)

    def assembly_home_full_page(self):
        """Create all object and assebly them to the home page"""
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

        soc_link = PageHeadSocLink.objects.create(
            soc_image=join(os.getcwd(), 'static/test_images/twitter.jpeg'),
            **_head_soc_link_data)
        soc_link2 = PageHeadSocLink.objects.create(
            soc_image=join(os.getcwd(), 'static/test_images/sharethis.jpeg'),
            **_head_soc_link_data)
        soc_link3 = PageHeadSocLink.objects.create(
            soc_image=join(os.getcwd(), 'static/test_images/linkedin.jpeg'),
            **_head_soc_link_data)
        header = PageHeaderBlock.objects.create(**_header_data)
        header.main_menus_elements.add(link_1, link_2, link_3)
        header.soc_links.add(soc_link, soc_link2, soc_link3)
        PageHelpBoxBlock.objects.create(**_help_box_data)
        PageWhatYouNeedBlock.objects.create(**_whatyouneed_block_data)
        footer_block = PageFooterBlock.objects.create(**_footer_block_data)
        footer_block.top_links.add(link_1, link_2, link_3)
        contact_address = Address.objects.create(**_address_block)
        footer_block.contact_address.add(contact_address)
        footer_block.a_link.add(link_element_1)

        # Create admin, if he is not exist
        if not User.objects.filter(is_staff=True):
            User.objects.create_superuser(
                'anvil8', 'anvil8@anvil8.com', 'densitron')

        # Login admin
        self.admin_login()

        # Click Add new Page
        self.selenium.find_element_by_css_selector('tr.model-page a.addlink')\
            .click()
        self.assertIn('Add page | Django site admin', self.selenium.title)

        # Fill the page data fields
        self.selenium.find_element_by_id('id_name')\
            .send_keys(_page_data['name'])
        self.selenium.find_element_by_id('id_description')\
            .send_keys(_page_data['description'])
        self.selenium.find_element_by_id('id_page_type')\
            .send_keys(_page_data['page_type'])
        self.selenium.find_element_by_id('id_title')\
            .send_keys(_page_data['title'])
        self.selenium.find_element_by_xpath(
            '//*[@id="id_header_block"]/option[2]').click()
        self.selenium.find_element_by_xpath(
            '//*[@id="id_what_you_need_block"]/option[2]').click()
        self.selenium.find_element_by_xpath(
            '//*[@id="id_help_box_block"]/option[2]').click()
        self.selenium.find_element_by_xpath(
            '//*[@id="id_footer_block"]/option[2]').click()
        self.selenium.find_element_by_xpath('//input[@value="Save"]').click()

        # Get Page Not Found Page
        self.selenium.get('{}{}'.format(
            self.live_server_url, "/page_not_found"))

        # Sleep 5 sec (For clarity, the correct display of the result)
        time.sleep(5)