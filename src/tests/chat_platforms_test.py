```python
import unittest
from src import chat_platforms

class TestChatPlatforms(unittest.TestCase):

    def setUp(self):
        self.platforms = chat_platforms.ChatPlatforms()

    def test_integrate_website(self):
        result = self.platforms.integrate_website()
        self.assertEqual(result, "Website integrated successfully")

    def test_integrate_mobile_app(self):
        result = self.platforms.integrate_mobile_app()
        self.assertEqual(result, "Mobile App integrated successfully")

    def test_integrate_whatsapp(self):
        result = self.platforms.integrate_whatsapp()
        self.assertEqual(result, "WhatsApp integrated successfully")

if __name__ == '__main__':
    unittest.main()
```