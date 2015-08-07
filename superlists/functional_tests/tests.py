from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = '0.0.0.0:8081'


class NewVisitorTest(StaticLiveServerTestCase):
    
    def setUp(self):
        self.get_firefox_browser_from_selenium_hub()
    
    def get_firefox_browser_from_selenium_hub(self):
        self.driver = webdriver.Remote(
            command_executor='http://192.168.99.100:4444/wd/hub',
            desired_capabilities={
                "browserName": "firefox"
            })
        self.driver.implicitly_wait(3)

    def check_for_row_in_list_table(self, row_text):
        table = self.driver.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def tearDown(self):
        self.driver.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage

        # self.live_server_url does not work with docker setup.  Don't know how to change url
        # away from "localhost" - Hardcoding the default port (that live_server_url uses) 
        # for the test - NOT a very good thing
        # Need to bind docker container to 2 ports when spinning up 8000 - normal 8081 - testing
        # print (self.live_server_url)
        # self.driver.get(self.live_server_url)
        self.driver.get('http://192.168.99.100:8081')
        

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.driver.title)
        header_text = self.driver.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.driver.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peackock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, she is taken to a new URL, and now the page lists
        # 1: Buy "peackock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.driver.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        
        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)
        inputbox = self.driver.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        ## We use a new browser session to make sure that no information
        ## of Edith's is coming through from cookies etc.
        self.driver.quit()
        self.get_firefox_browser_from_selenium_hub()
        
        # Francis visits the home page.  There is no sign of Edith's list
        self.driver.get('http://192.168.99.100:8081')
        page_text = self.driver.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fl', page_text)
        
        # Francis starts a new list by entering a new item.  He is less interesting than Edith ...
        inputbox = self.driver.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        
        # Francis gets his own unique URL
        francis_list_url = self.driver.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)
        
        # Again, there is no trace of Edith's list
        page_text = self.driver.find_element_by_tag_name('body').text
        self.driver.implicitly_wait(3)
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)
        
        # Satisfied, they both go back to sleep
        
    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.driver.get('http://192.168.99.100:8081')
        self.driver.set_window_size(1024, 758)
        
        # She notices the input box is nicely centered
        inputbox = self.driver.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2, 
            512,
            delta=5
        )
        
        # She starts a new list and see the input is nicely centered there too
        inputbox.send_keys('testing\n')
        inputbox = self.driver.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2, 
            512,
            delta=5
        )
        