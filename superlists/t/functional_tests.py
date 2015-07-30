from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='http://192.168.99.100:4444/wd/hub',
            desired_capabilities={
                "browserName": "firefox"
            })
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()
        
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.driver.get('http://192.168.99.100:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.driver.title)
        self.fail('Finish the test!')

        # She is invited to enter a to-do item straight away

        # She types "Buy peackock feathers" into a text box

        # When she hits enter, the page updates, and now the page lists
        # 1: Buy "peackock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep
if __name__ == '__main__':
    unittest.main(warnings='ignore')