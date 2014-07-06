# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from os import environ as env
import unittest


class SeleniumMixin:
    def setUp(self):
        super().setUp()
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
        self.browser.quit()
        super().tearDown()


class NewVisitorTest(SeleniumMixin, unittest.TestCase):
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes to check
        # out it's homepage.
        self.browser.get(self.url)
        self.assertIn('To-Do', self.browser.title)

        # She is invited to enter to-do item straight away.

        # She types "Buy peacock feathers" into a text box (Edith's hobby is
        # tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists "1:
        # Buy peacock feathers" as an item in a to-do list.

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)

        # The page updates again, and now shows both items on her list.

        # Edith wonders whether the site will remember her list. The she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep.
        self.fail("Finish the test!")


if __name__ == '__main__':
    unittest.main()
