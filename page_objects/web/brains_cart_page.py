from playwright.sync_api import Page

class BrainsCartPage:
    
    def __init__(self,page:Page):
        self.page=page
        self.text_header = page.locator("[class='text-xl font-black font-oswald mb-5']")
        self.products_names = page.locator("//h3[@class='font-bold font-oswald text-lg']")
        self.remove_buttons = page.locator("[class^='text-red-500 ']")
        self.products_prices = page.locator("p[class='font-bold font-oswald text-lg']")
        self.products_total_prices = page.locator("[class='font-bold text-lg font-oswald']")
        self.checkout_button = page.locator("[class^='flex items-center gap-2 b']")
        self.continue_shopping_button = page.locator("[class='text-sm']")
        self.quantity = page.locator("[class='border rounded px-3 py-1 text-gray-500']")
        self.increase_button = page.locator("//button[text()='+']")
        self.reduce_button = page.locator("//button[text()='-']")
        self.empty_cart_message = page.locator("[class^='text-2xl mx']")
        self.confirm_remove_button = page.locator("[data-slot='dialog-close']").nth(1)
