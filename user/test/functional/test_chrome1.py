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
        #cls.selenium.implicity_wait(10)
        cls.username = "toutou"
        cls.email = "toutou@gmail.com"
        cls.password = "Toutou!*1914"


    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_user_register_and_login(self):
        self.selenium.get("http://127.0.0.1:8000/user/register")
        #user_url = self.live_server_url  
        #self.selenium.find_elements_by_css_selector("#register-link").click()

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
        self.selenium.find_element_by_id("button-submit-register").click()
        time.sleep(10)


        self.selenium.find_element_by_id("id-username").send_keys(
            self.username
        )
        self.selenium.find_element_by_id("id-password").send_keys(
            self.password
        )
        self.selenium.find_element_by_id("button-submit-login").click()
        # A faire appuer sur le bouton et rajouter pour valider 


        #self.assertEqual(self.selenium.current_url, user_url)
       



