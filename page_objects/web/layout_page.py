from playwright.sync_api import Page



class BrainsFooter:
    def __init__(self,page:Page):
        self.page = page
        self.footer_social_links = page.locator("div>[target='_blank']")




class Brainsheader:
    def __init__(self,page:Page):
        self.page = page
        self.shopping_cart_icon = page.locator("//div[@class='profile flex items-center gap-4']/span")
        self.user_icon = page.locator("[aria-haspopup='menu']")
        self.favorite_products = page.locator("[role='menuitem']").first
        self.logout_button = page.locator("[role='menuitem']").last
        self.products_in_cart = page.locator("[class^='bg-qa-clr text-[13px]']")
        self.confirm_logout = page.locator("//button[text()='Logout']")
        