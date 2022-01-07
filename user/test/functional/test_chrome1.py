from selenium import webdriver
from django.contrib.staticfiles.testing import LiveServerTestCase
from webdriver_manager.chrome import ChromeDriverManager
from django.contrib.auth import get_user_model
from django.urls import reverse
from config.settings import BASE_DIR


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
        #cls.selenium.implicity_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_user_register_and_login(self):
        self.selenium.get("http://127.0.0.1:8000/user/register")
        home_url = self.live_server_url  
        self.selenium.find_elements_by_css_selector("#register-link").click()

        self.selenium.find_element_by_css_selector("#id-username").send_keys(
            "toto"
        )
        self.selenium.find_element_by_css_selector("#id-email").send_keys(
            "toto@gmail.com"
        )
        self.selenium.find_element_by_css_selector("#id-password1").send_keys(
            "Saturn!*1584"
        )
        self.selenium.find_element_by_css_selector("#id-password2").send_keys(
            "Saturn!*1584"
        )
        self.selenium.find_elements_by_css_selector("#button-submit-register").click()

        self.assertEqual(self.selenium.current_url, home_url)
       



