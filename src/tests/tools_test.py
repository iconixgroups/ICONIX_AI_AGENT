```python
import unittest
from src.tools import useAnalyticsTool, integrateChatPlatform, connectAIPlatform

class TestTools(unittest.TestCase):

    def setUp(self):
        self.analytics_tool = "Google Analytics"
        self.chat_platform = "WhatsApp"
        self.ai_platform = "OpenAI"

    def test_useAnalyticsTool(self):
        result = useAnalyticsTool(self.analytics_tool)
        self.assertEqual(result, f"Analytics tool {self.analytics_tool} has been used.")

    def test_integrateChatPlatform(self):
        result = integrateChatPlatform(self.chat_platform)
        self.assertEqual(result, f"Chat platform {self.chat_platform} has been integrated.")

    def test_connectAIPlatform(self):
        result = connectAIPlatform(self.ai_platform)
        self.assertEqual(result, f"AI platform {self.ai_platform} has been connected.")

if __name__ == '__main__':
    unittest.main()
```