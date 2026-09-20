from playwright.sync_api import Page , expect
from CIVIC.pageobject.homepage import Homepage
from CIVIC.config import Config

def test_tc_00001(page:Page):
    """
    To verify - OPENLOCAL LOGO availability
    """

    # Create page object
    home_page = Homepage(page)

    # Call URL
    page.goto(Config.base_url)

    # Logo assertion
    openlocallogo = home_page.chcek_logo()
    expect(openlocallogo).to_be_visible()