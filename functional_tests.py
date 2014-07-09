# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from os import environ as env
import unittest
from datetime import datetime


class SeleniumMixin:
    @staticmethod
    def screenshot_on_fail(func):
        def wrapper(self, *args, **kwargs):
            try:
                func(self, *args, **kwargs)
            except:
                self.take_screenshot = True
                raise
        return wrapper

    def setUp(self):
        super().setUp()
        self.take_screenshot = False
        self.url = 'http://{}:{}'.format(
            env['YADS_PORT_8000_TCP_ADDR'],
            env['YADS_PORT_8000_TCP_PORT'],
        )
        self.browser = webdriver.Remote(
            'http://{}:{}/wd/hub'.format(
                env['SELENIUM_PORT_4444_TCP_ADDR'],
                env['SELENIUM_PORT_4444_TCP_PORT'],
            ),
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.browser.implicitly_wait(3)

    def tearDown(self):
        if self.take_screenshot:
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.browser.get_screenshot_as_file('screenshot-%s.png' % now)
        self.browser.quit()
        super().tearDown()


class NewVisitorTest(SeleniumMixin, unittest.TestCase):
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    @SeleniumMixin.screenshot_on_fail
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes to check
        # out it's homepage.
        self.browser.get(self.url)

        # She notices the page title and header mention to-do list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter to-do item straight away.
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            input_box.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby is
        # tying fly-fishing lures)
        input_box.send_keys("Buy peacock feathers")

        # When she hits enter, the page updates, and now the page lists "1:
        # Buy peacock feathers" as an item in a to-do list.
        input_box.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys("Use peacock feathers to make a fly")
        input_box.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list.
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # Edith wonders whether the site will remember her list. The she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep.
        self.fail("Finish the test!")


if __name__ == '__main__':
    unittest.main()
