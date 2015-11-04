'''Base Class for Selenium Test Classes

'''
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

import os
os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = '0.0.0.0:8081'

import sys

DOCKER_TEST_SERVER_URL = 'http://192.168.99.100:8081'

DEFAULT_WAIT = 5

class FunctionalTest(StaticLiveServerTestCase):
    '''Base Class for Selenium Test Classes'''

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        ## hard code for docker setup because boot2docker does not use localhost
        # self.live_server_url does not work with docker setup.  Don't know how to change url
        # away from "localhost" - Hardcoding the default port (that live_server_url uses)
        # for the test - NOT a very good thing
        # Need to bind docker container to 2 ports when spinning up 8000 - normal 8081 - testing
        # print (self.live_server_url)
        # self.driver.get(self.live_server_url) - update from self to cls. due to setUpClass
        if os.environ['TRAVIS_CI'] == 'true':
            cls.server_url = cls.live_server_url
        else:
            cls.server_url = DOCKER_TEST_SERVER_URL

    @classmethod
    def tearDownClass(cls):
        if os.environ['TRAVIS_CI'] == 'true':
            if cls.server_url == cls.live_server_url:
                super().tearDownClass()
        else:
            if cls.server_url == DOCKER_TEST_SERVER_URL:
                super().tearDownClass()

    def setUp(self):
        if os.environ['TRAVIS_CI'] == 'true':
            self.driver = webdriver.Firefox()
            self.driver.implicitly_wait(DEFAULT_WAIT)
            self.driver.set_page_load_timeout(DEFAULT_WAIT)
        else:
            self.get_firefox_browser_from_selenium_hub()


    def get_firefox_browser_from_selenium_hub(self):
        '''setup firefox browser instance for selenium use'''
        self.driver = webdriver.Remote(
            command_executor='http://192.168.99.100:4444/wd/hub',
            desired_capabilities={
                "browserName": "firefox"
            })
        self.driver.implicitly_wait(5)
        self.driver.implicitly_wait(DEFAULT_WAIT)
        self.driver.set_page_load_timeout(DEFAULT_WAIT)
        

    def check_for_row_in_list_table(self, row_text):
        ''' checks for value in table'''
        table = self.driver.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def tearDown(self):
        '''tear down to run after test suite run'''
        self.driver.quit()

    def get_item_input_box(self):
        ''' return selenium element'''
        return self.driver.find_element_by_id('id_text')
