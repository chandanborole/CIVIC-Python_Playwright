from playwright.sync_api import Page

# Page object class for HomePage

class Homepage:

    # Constructor
    def __init__(self , page:Page):
        self.page = page

        # Locators declaration for home page
        self.homepage_logo_openlocal = self.page.locator(".style-module__KSt7QW__logoContainer")

    # Action methods
    def chcek_logo(self):
        return self.homepage_logo_openlocal
