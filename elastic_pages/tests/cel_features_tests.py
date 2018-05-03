"""Module Elastic Pages Selenium unittest
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
import operator
import random
import string

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.db.models import Q

from selenium import webdriver
from functools import reduce
import time
from selenium.webdriver.common.keys import Keys
from elastic_pages.models import Page

from products.models import TftProduct, Product, Technology, Category


class MySeleniumFeatureTests(StaticLiveServerTestCase):
    """Need pre-created: Home Page + what_you_need Block"""
    serialized_rollback = True

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(MySeleniumFeatureTests, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(MySeleniumFeatureTests, self).tearDown()

    def test_quick_access_to_a_product_whtc(self):
        """ Test
        Feature: Quick access to a product or set of products using
                 “Custom” toolbar
        Scenario: To get matched by width, height, touch and color products
        """
        self.selenium.get('{}'.format(self.live_server_url))

        _find_product = TftProduct.objects.first()

        if _find_product.colour:
            self.selenium.find_element_by_id('custom-colour').click()
        _find_product_touch = True
        if _find_product.touch:
            self.selenium.find_element_by_id('custom-touch').click()
            _find_product_touch = False
        time.sleep(0.5)
        self.selenium.find_element_by_id('custom-width')\
            .send_keys(_find_product.dimension_w)
        time.sleep(0.5)
        self.assertEqual(
            int(self.selenium.find_element_by_id('find_product').text),
            TftProduct.objects.filter(
                colour=_find_product.colour,
                touch__isnull=_find_product_touch,
                dimension_w=_find_product.dimension_w).count()
        )
        self.selenium.find_element_by_id('custom-height')\
            .send_keys(_find_product.dimension_h)
        time.sleep(3)
        self.assertEqual(
            int(self.selenium.find_element_by_id('find_product').text),
            TftProduct.objects.filter(
                colour=_find_product.colour,
                touch__isnull=_find_product_touch,
                dimension_h=_find_product.dimension_h,
                dimension_w=_find_product.dimension_w).count()
        )

        self.selenium.find_element_by_xpath(
            '//*[@id="what_need_product_filter"]/a').click()

        self.assertEqual(
            len(self.selenium.find_elements_by_css_selector(
                '#content > div > div.content > div.product-box'))-1,
            TftProduct.objects.filter(
                colour=_find_product.colour,
                touch__isnull=_find_product_touch,
                dimension_h=_find_product.dimension_h,
                dimension_w=_find_product.dimension_w).count()
        )
        self.assertEqual(
            self.selenium.find_element_by_css_selector(
                '#content > div > div.content > div:nth-child(1) > a').text,
            TftProduct.objects.filter(
                colour=_find_product.colour,
                touch__isnull=_find_product_touch,
                dimension_h=_find_product.dimension_h,
                dimension_w=_find_product.dimension_w).first().get_name()
        )

    def test_quick_access_to_a_product_dtc(self):
        """ Test
        Feature: Quick access to a product or set of products using
                 “Custom” toolbar
        Scenario: To get products matched by diagonal, touch and color
        """
        self.selenium.get('{}'.format(self.live_server_url))

        _find_product = TftProduct.objects.first()

        self.selenium.find_element_by_id('custom-diagonal')\
            .send_keys(_find_product.size)

        _find_product_touch = False
        if not _find_product.touch:
            _find_product_touch = True
        time.sleep(0.5)
        self.assertEqual(
            int(self.selenium.find_element_by_id('find_product').text),
            TftProduct.objects.filter(
                touch__isnull=True,
                size=_find_product.size,
                colour=False).count()
        )

        self.selenium.find_element_by_id('custom-touch').click()
        time.sleep(0.5)
        self.assertEqual(
            int(self.selenium.find_element_by_id('find_product').text),
            TftProduct.objects.filter(
                touch__isnull=False,
                size=_find_product.size,
                colour=False).count()
        )

        self.selenium.find_element_by_id('custom-colour').click()
        time.sleep(0.5)
        self.assertEqual(
            int(self.selenium.find_element_by_id('find_product').text),
            TftProduct.objects.filter(
                touch__isnull=False,
                size=_find_product.size,
                colour=True).count()
        )

        if not _find_product.colour:
            self.selenium.find_element_by_id('custom-colour').click()
        if not _find_product.touch:
            self.selenium.find_element_by_id('custom-touch').click()
        time.sleep(0.5)
        self.assertEqual(
            int(self.selenium.find_element_by_id('find_product').text),
            TftProduct.objects.filter(
                colour=_find_product.colour,
                touch__isnull=_find_product_touch,
                size=_find_product.size).count()
        )

        self.selenium.find_element_by_xpath(
            '//*[@id="what_need_product_filter"]/a').click()

        self.assertEqual(
            len(self.selenium.find_elements_by_css_selector(
                '#content > div > div.content > div.product-box'))-1,
            TftProduct.objects.filter(
                colour=_find_product.colour,
                touch__isnull=_find_product_touch,
                size=_find_product.size)[:11].count()
        )
        self.assertEqual(
            self.selenium.find_element_by_css_selector(
                '#content > div > div.content > div:nth-child(1) > a').text,
            TftProduct.objects.filter(
                colour=_find_product.colour,
                touch__isnull=_find_product_touch,
                size=_find_product.size).first().get_name()
        )

    def test_quick_access_to_a_product_empty(self):
        """ Test
        Feature: Quick access to a product or set of products using
                 “Custom” toolbar
        Scenario: To get matched products by empty form
        """
        self.selenium.get('{}'.format(self.live_server_url))

        self.selenium.find_element_by_xpath(
            '//*[@id="what_need_product_filter"]/a').click()

        self.assertEqual(
            len(self.selenium.find_elements_by_css_selector(
                '#content > div > div.content > div.product-box'))-1,
            TftProduct.objects.all()[:11].count()
        )

    def test_matches_counter_in_product_form(self):
        """ Test
        Feature: Matches counter in  “Custom” toolbar
        Scenario: See count of matched products
        """
        self.selenium.get('{}'.format(self.live_server_url))

        self.selenium.find_element_by_id('custom-touch').click()
        time.sleep(0.5)
        self.assertEqual(
            int(self.selenium.find_element_by_id('find_product').text),
            TftProduct.objects.filter(
                touch__isnull=False, colour=False).count()
        )
        self.selenium.find_element_by_id('custom-touch').click()
        time.sleep(0.5)
        self.assertEqual(
            int(self.selenium.find_element_by_id('find_product').text),
            TftProduct.objects.filter(
                touch__isnull=True, colour=False).count()
        )
        self.selenium.find_element_by_id('custom-colour').click()
        time.sleep(0.5)
        self.assertEqual(
            int(self.selenium.find_element_by_id('find_product').text),
            TftProduct.objects.filter(touch__isnull=True, colour=True).count()
        )
        self.selenium.find_element_by_id('custom-touch').click()
        time.sleep(0.5)
        self.assertEqual(
            int(self.selenium.find_element_by_id('find_product').text),
            TftProduct.objects.filter(
                touch__isnull=False, colour=True).count()
        )

    def test_quick_access_to_product_by_existing_toolbar_by_id(self):
        """ Test
        Feature: Quick access to product or set of products using
        ‘Existing’ toolbar
        Scenario: To get existing product by #
        """
        self.selenium.get('{}'.format(self.live_server_url))

        _find_product = TftProduct.objects.first()

        self.selenium.find_element_by_id('existing')\
            .send_keys(_find_product.id)
        self.selenium.find_element_by_id('find_key_product').click()
        self.assertEqual(
            _find_product.get_name(),
            self.selenium.find_element_by_tag_name('h2').text)

    def test_quick_access_to_product_by_existing_toolbar_by_key(self):
        """ Test
        Feature: Quick access to product or set of products using
        ‘Existing’ toolbar
        Scenario: To get existing product by keyword
        """
        self.selenium.get('{}'.format(self.live_server_url))

        _find_product = TftProduct.objects.first()

        self.selenium.find_element_by_id('existing')\
            .send_keys(_find_product.name)
        self.selenium.find_element_by_id('find_key_product').click()

        self.assertEqual(
            len(self.selenium.find_elements_by_css_selector(
                '#content > div > div.content > div.product-box'))-1,
            TftProduct.objects.filter(reduce(
                operator.and_,
                (Q(name__contains=x)
                    for x in _find_product.name.split(' ')))
                )[:11].count()
        )

    def test_quick_access_to_product_by_existing_toolbar_by_wrong_key(self):
        """ Test
        Feature: Quick access to product or set of products using
        ‘Existing’ toolbar
        Scenario: To get nonexistent product by # or keyword
        """
        self.selenium.get('{}'.format(self.live_server_url))

        self.selenium.find_element_by_id('existing')\
            .send_keys(''.join(random.choice(string.ascii_letters)
                               for x in range(20)))
        self.selenium.find_element_by_id('find_key_product').click()

        self.assertEqual(
            len(self.selenium.find_elements_by_css_selector(
                '#content > div > div.content > div.product-box'))-1,
            TftProduct.objects.all()[:11].count()
        )

        self.selenium.get('{}'.format(self.live_server_url))

        self.selenium.find_element_by_id('existing')\
            .send_keys(Product.objects.last().id+1)
        self.selenium.find_element_by_id('find_key_product').click()

        self.assertEqual(
            len(self.selenium.find_elements_by_css_selector(
                '#content > div > div.content > div.product-box'))-1,
            TftProduct.objects.all()[:11].count()
        )

    def test_quick_access_to_product_by_popular_toolbar_by_name(self):
        """ Test
        Feature: Quick access to product or set of products using
        “Popular” toolbar
        Scenario: To choose product from the “Popular List”
        """
        self.selenium.get('{}'.format(self.live_server_url))
        product_elem = self.selenium.find_element_by_css_selector(
            '#content > div.content-box.what_you_need > div > '
            'div:nth-child(3) > ul > li:nth-child(1) > a')
        product_text = product_elem.text
        product_elem.click()
        self.assertEqual(product_text,
                         self.selenium.find_element_by_tag_name('h2').text)

    def test_quick_access_to_product_by_popular_toolbar_by_full_catalog(self):
        """ Test
        Feature: Quick access to product or set of products using
        “Popular” toolbar
        Scenario: To choose product from the “Full catalog”
        """
        self.selenium.get('{}'.format(self.live_server_url))
        self.selenium.find_element_by_css_selector(
            'div.content-box.what_you_need > div > div:nth-child(3) > a')\
            .click()
        self.assertEqual(
            len(self.selenium.find_elements_by_css_selector(
                'div.product-bar-wrapper > div.product_in_bar')),
            Technology.objects.all().count())

    def test_choose_a_category(self):
        """ Test
        Feature: Categories and subcategories menu
        Scenario: Choose a category
        """
        self.selenium.get('{}'.format(self.live_server_url))
        self.selenium.find_element_by_css_selector(
            'div.content-box.what_you_need > div > div:nth-child(3) > a')\
            .click()
        self.assertEqual(
            len(self.selenium.find_elements_by_css_selector(
                'div.product-bar-wrapper > div.product_in_bar')),
            Technology.objects.all().count())
        self.selenium.find_elements_by_css_selector(
            'div.product_in_bar > div > a')[1].click()

    def test_choose_a_subcategory(self):
        """ Test
        Feature: Categories and subcategories menu
        Scenario: Immediately select a subcategory
        """
        self.selenium.get('{}'.format(self.live_server_url))
        self.selenium.find_element_by_css_selector(
            'div.content-box.what_you_need > div > div:nth-child(3) > a')\
            .click()
        self.assertEqual(
            len(self.selenium.find_elements_by_css_selector(
                'div.product-bar-wrapper > div.product_in_bar')),
            Technology.objects.all().count())
        self.selenium.find_elements_by_partial_link_text('TFT')[1].click()
        self.assertEqual(
            len(self.selenium.find_elements_by_css_selector(
                '#content > div > div.content > div.product-box'))-1,
            TftProduct.objects.all()[:11].count()
        )

    def test_select_a_subcategory(self):
        """ Test
        Feature: Subcategories menu
        Scenario: Select a subcategory
        """
        tft_id = Technology.objects.get(name='TFTs').id
        self.selenium.get('{}/{}/{}/'.format(
            self.live_server_url, 'products', tft_id))
        count = 0
        for s in self.selenium.find_elements_by_css_selector(
                'div.product-category-header > ol > li'):
            self.selenium.find_elements_by_css_selector(
                'div.product-category-header > ol > li')[count].click()
            count += 1
            text = self.selenium.find_element_by_css_selector(
                'div.product-category-header > ol > li.active > h3').text
            self.selenium.find_element_by_css_selector(
                'div.product_in_bar.active > div.product_in_bar_column.halfed'
                ' > a.color-button.orange').click()
            self.assertEqual(
                len(self.selenium.find_elements_by_css_selector(
                    '#content > div > div.content > div.product-box'))-1,
                TftProduct.objects.filter(category__name=text)[:11].count()
            )
            self.selenium.get('{}/{}/{}/'.format(
                self.live_server_url, 'products', tft_id))

        self.selenium.find_element_by_css_selector(
            'div.product_in_bar.active > div.product_in_bar_column.halfed > '
            'a.color-button.blue').click()
        assert 'Bespoke Orders' in self.selenium.title

    def test_search_toolbar_on_the_wizard_page(self):
        """ Test
        Feature: Search toolbar on the Wizard page
        Scenario: To get existing product by #
        """
        self.selenium.get('{}{}'.format(
            self.live_server_url, '/product_found/'))

        _find_product = TftProduct.objects.first()

        self.selenium.find_element_by_id('existing')\
            .send_keys(_find_product.id)
        self.selenium.find_element_by_id('find_key_product').click()
        self.assertEqual(
            _find_product.get_name(),
            self.selenium.find_element_by_tag_name('h2').text)
        self.selenium.get('{}'.format(self.live_server_url))

        self.selenium.find_element_by_id('existing')\
            .send_keys(_find_product.name)
        self.selenium.find_element_by_id('find_key_product').click()

        self.assertEqual(
            len(self.selenium.find_elements_by_css_selector(
                '#content > div > div.content > div.product-box'))-1,
            TftProduct.objects.filter(reduce(
                operator.and_,
                (Q(name__contains=x)
                    for x in _find_product.name.split(' ')))
                )[:11].count()
        )

    def test_filter_toolbar_on_wizard_filter_by_diagonal(self):
        """ Test
        Feature: Filter toolbar on the Wizard page
        Scenario: Filter products by diagonal param
        """
        self.selenium.get('{}{}'.format(
            self.live_server_url, '/product_found/'))
        self.selenium.find_element_by_css_selector(
            '#content > div > div.sidebar > div:nth-child(8)').click()
        self.selenium.implicitly_wait(3)
        self.selenium.find_element_by_id('size').send_keys('4.30')
        self.selenium.find_element_by_id('size').send_keys(Keys.ENTER)
        assert 'Products found' in self.selenium.title
        self.assertEqual(
            len(self.selenium.find_elements_by_css_selector(
                '#content > div > div.content > div.product-box'))-1,
            Product.objects.filter(size='4.30')[:11].count()
        )

    def test_clear_all_filters_on_wizard(self):
        """ Test
        Feature: Filter toolbar on the Wizard page
        Scenario: Clear all filters
        """
        self.selenium.get('{}{}'.format(
            self.live_server_url, '/product_found/'))
        self.selenium.find_element_by_css_selector(
            '#content > div > div.sidebar > div:nth-child(8)').click()
        self.selenium.implicitly_wait(3)
        self.selenium.find_element_by_id('size').send_keys('4.30')
        self.selenium.find_element_by_id('size').send_keys(Keys.ENTER)
        self.assertEqual(
            len(self.selenium.find_elements_by_css_selector(
                '#content > div > div.content > div.product-box'))-1,
            Product.objects.filter(size='4.30')[:11].count()
        )
        self.selenium.find_element_by_css_selector(
            '#content > div > div.sidebar > a').click()
        self.assertEqual(
            len(self.selenium.find_elements_by_css_selector(
                '#content > div > div.content > div.product-box'))-1,
            Product.objects.all()[:11].count()
        )

    def test_sort_product_by_size_lowest(self):
        """ Test
        Feature: Filter toolbar on the Wizard page
        Scenario: Clear all filters
        """
        self.selenium.get('{}{}'.format(
            self.live_server_url, '/product_found/'))

        self.assertEqual(
            len(self.selenium.find_elements_by_css_selector(
                '#content > div > div.content > div.product-box'))-1,
            Product.objects.all()[:11].count()
        )
        size = self.selenium.find_element_by_name('product-size-inches')
        self.assertEqual(size.find_element_by_css_selector(
            'span:last-child').text, '4.30')
        self.selenium.find_element_by_id('sort_product').click()
        self.selenium.find_element_by_id('sort_product').\
            find_element_by_css_selector('option:last-child').click()
        time.sleep(0.5)
        size = self.selenium.find_element_by_name('product-size-inches')
        self.assertEqual(size.find_element_by_css_selector(
            'span:last-child').text, '4.20')