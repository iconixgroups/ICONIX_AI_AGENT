import requests

class ChatPlatformIntegration:
    def __init__(self, platform, agent):
        self.platform = platform
        self.agent = agent

    def integrate_with_website(self):
        # Integration code for website goes here
        pass

    def integrate_with_mobile_app(self):
        # Integration code for mobile app goes here
        pass

    def integrate_with_whatsapp(self):
        # Integration code for WhatsApp goes here
        pass

    def integrate(self):
        if self.platform == 'Website':
            self.integrate_with_website()
        elif self.platform == 'Mobile App':
            self.integrate_with_mobile_app()
        elif self.platform == 'WhatsApp':
            self.integrate_with_whatsapp()
        else:
            print("Invalid platform")

def integrateChatPlatform(platform, agent):
    chat_platform_integration = ChatPlatformIntegration(platform, agent)
    chat_platform_integration.integrate()