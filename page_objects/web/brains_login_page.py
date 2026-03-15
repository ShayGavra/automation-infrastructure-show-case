from playwright.sync_api import Page


class BrainsLoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.email_field = page.locator("[id='email']")
        self.password_field = page.locator("[id='password']")
        self.login_buttton = page.locator("[type='submit']")
        self.email_error_field = page.locator("[class='text-red-500 text-sm mt-1']")
        self.password_error_field = page.locator("[class='text-red-500 text-sm mt-1']")