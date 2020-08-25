from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import random
import string

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        
        # Load up the Admin page
        self.browser.get('http://127.0.0.1:8000/admin')

        # The user types their username into the username input
        username_input = self.browser.find_element_by_id('id_username')  
        username_input.send_keys('test')  

        # The user types in their password into the password and presses enter to log in
        password_input = self.browser.find_element_by_id('id_password')  
        password_input.send_keys('temppassword123')  
        password_input.send_keys(Keys.ENTER)  
        time.sleep(1)  

        # Once logged in the user goes to the add course page
        self.browser.get("http://127.0.0.1:8000/admin/cv/course/add/")

        # The user enters a title
        title_input = self.browser.find_element_by_id('id_title')  
        title = get_random_string(8)
        title_input.send_keys(title)

        # And a grade
        grade_input = self.browser.find_element_by_id('id_grade')
        grade_input.send_keys("100")

        # And selects year 1
        year_select = self.browser.find_element_by_id('id_year')
        all_options = year_select.find_elements_by_tag_name("option")
        for option in all_options:
            if(option.get_attribute("value") == "year1"):
                option.click()
     
        # The user presses enter to save the course
        grade_input.send_keys(Keys.ENTER)  
        time.sleep(1)  

        # The user goes to the CV page to check if the new data is present
        self.browser.get('http://127.0.0.1:8000/cv')

        # The user looks in the Year1 section of university modules

        year1_div = self.browser.find_element_by_id("year1")
        
        # The user checks if the course they added is there
        self.assertIn(title, year1_div.text)

def get_random_string(length):
    letters = string.ascii_lowercase
    return(''.join(random.choice(letters) for i in range(length)))
    


if __name__ == '__main__':  
    unittest.main(warnings='ignore')  