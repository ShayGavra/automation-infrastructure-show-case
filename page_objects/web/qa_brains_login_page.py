from playwright.sync_api import Page


class QaBrainsLoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.email_field = page.locator("[id='email']")
        self.password_field = page.locator("[id='password']")
        self.login_buttton = page.locator("[type='submit']")
        