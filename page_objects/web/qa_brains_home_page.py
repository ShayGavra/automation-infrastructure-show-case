from playwright.sync_api import Page


class QaBrainsHomePage:
    def __init__(self,page:Page):
        self.page = page
        self.products = page.locator("[class^='text-lg block']")
        self.prices = page.locator("[class^='text-lg font']")
        