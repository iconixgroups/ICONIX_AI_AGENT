```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LandingPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_signup_button(self):
        driver = self.driver
        driver.get("http://www.iconixai.com")
        self.assertIn("ICONIX AI Agent", driver.title)
        elem = driver.find_element_by_id("signupButton")
        self.assertIsNotNone(elem)

    def test_login_button(self):
        driver = self.driver
        driver.get("http://www.iconixai.com")
        self.assertIn("ICONIX AI Agent", driver.title)
        elem = driver.find_element_by_id("loginButton")
        self.assertIsNotNone(elem)

    def test_landing_page_video(self):
        driver = self.driver
        driver.get("http://www.iconixai.com")
        self.assertIn("ICONIX AI Agent", driver.title)
        elem = driver.find_element_by_tag_name("video")
        self.assertIsNotNone(elem)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
```