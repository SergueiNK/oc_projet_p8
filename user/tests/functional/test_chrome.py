from selenium import webdriver
import time
from django.contrib.staticfiles.testing import LiveServerTestCase
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('window-size=1920x1080')


class ChromeFunctionalTestUser(LiveServerTestCase):
    """Functional User test for the login and registration"""

    @classmethod
    def setUpClass(cls):
        """Tests variables and config"""
        super().setUpClass() 
        cls.selenium = webdriver.Chrome(ChromeDriverManager().install())
        #Create data for test
        cls.username = "koukou"
        cls.email = "koukou@gmail.com"
        cls.password = "Koukou!*1914"


    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_user_register_and_login(self):
        """User will be register, login and have an acces to home page"""

        # Acces to live server user page
        self.selenium.get("http://127.0.0.1:8000/user/register")

        # Completing the form for user register
        self.selenium.find_element_by_id("id_username").send_keys(
            self.username
        )
        self.selenium.find_element_by_id("id_email").send_keys(
            self.email
        )
        self.selenium.find_element_by_id("id_password1").send_keys(
            self.password
        )
        self.selenium.find_element_by_id("id_password2").send_keys(
            self.password
        )
        # Submit button for form of user register
        self.selenium.find_element_by_id("button-submit-register").click()
        time.sleep(3)
        
        # Completing the form for user login
        self.selenium.find_element_by_id("id-username").send_keys(
            self.username
        )
        self.selenium.find_element_by_id("id-password").send_keys(
            self.password
        )
        # Submit button for form of user login
        self.selenium.find_element_by_id("button-submit-login").click()

       



