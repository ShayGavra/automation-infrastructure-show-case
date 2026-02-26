from playwright.sync_api import Page


class BrainsProductsPage:
    def __init__(self,page:Page):
        self.page = page
        self.products_names = page.locator("[class^='text-lg block']")
        self.prices = page.locator("[class^='text-lg font']")
        self.order_by_button = page.locator("[data-slot='popover-trigger']")
        self.order_by_search = page.locator("[data-slot='command-input']")
        self.order_by_options = page.locator("[data-slot='command-item']")
        self.favorites_buttons = page.locator("[class='w-5 h-5']")
        self.add_to_cart_buttons = page.locator("[class^='border inline']")
        self.products_heading = page.locator("[class^='text-xl font-black']")
        