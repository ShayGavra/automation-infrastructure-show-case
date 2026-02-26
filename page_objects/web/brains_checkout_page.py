
from playwright.sync_api import Page

class BrainsCheckoutPage:
    def __init__(self,page:Page):
        self.page=page
        self.text_checkot = page.locator("[class='text-xl font-black font-oswald mb-5']")
        self.email_field = page.locator("[class='form-control bg-gray-200 cursor-no-drop opacity-80']")
        self.frist_name_field = page.locator("[placeholder='Ex. John']")
        self.last_name_field = page.locator("[placeholder='Ex. Doe']")
        self.zip_code = page.locator("[type='text']").last
        self.continue_button = page.locator("[class^='flex items-center gap-2 b']")
        self.checkout_list = page.locator("[class^='flex items-center justify-between']")
        self.checkout_price = page.locator("p[class='font-bold font-oswald text-lg']")
        self.total_price = page.locator("//*[@class='group'][3]/p[3]")

        
