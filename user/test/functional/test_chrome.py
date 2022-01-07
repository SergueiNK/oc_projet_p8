import sys

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from config.settings import BASE_DIR
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('window-size=1920x1080')


class ChromeFunctionalTestUser(StaticLiveServerTestCase):
    """Functional User test for the login and registration"""

    @classmethod
    def setUpClass(cls):
        """Tests variables and config"""
        super().setUpClass() 
        cls.driver = webdriver.Chrome(
            executable_path=str(BASE_DIR / "webdrivers" / "chromedriver"),
        options=chrome_options,)
        
        cls.username = "toto"
        cls.email = "toto@gmail.com"
        cls.password1 = "Saturn!*1584"
        cls.password2 = "Saturn!*1584"
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.driver.quit()    


    def test_user_register_and_login(self):
        """Test of user register and login """

        self.driver.get(self.live_server_url)

        self.driver.find_elements_by_css_selector("#register-link").click()
        self.driver.find_element_by_css_selector("#id-username").send_keys(
            self.username
        )
        self.driver.find_element_by_css_selector("#id-email").send_keys(
            self.email
        )
        self.driver.find_element_by_css_selector("#id-password1").send_keys(
            self.password1
        )
        self.driver.find_element_by_css_selector("#id-password2").send_keys(
            self.password2
        )
        self.driver.find_elements_by_css_selector("#button-submit-register").click()



