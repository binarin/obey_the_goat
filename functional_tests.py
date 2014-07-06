# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from os import environ as env

browser = webdriver.Remote(
    'http://{}:{}/wd/hub'.format(
        env['SELENIUM_PORT_4444_TCP_ADDR'],
        env['SELENIUM_PORT_4444_TCP_PORT'],
    ),
    desired_capabilities=DesiredCapabilities.CHROME
)

url = 'http://{}:{}'.format(
    env['YADS_PORT_8000_TCP_ADDR'],
    env['YADS_PORT_8000_TCP_PORT'],
)
browser.get(url)
assert 'Django' in browser.title
