from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):        

    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.driver.get(self.server_url)
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
