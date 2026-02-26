import allure
from playwright.sync_api import Page
from extensions.ui_actions import UIActions
from extensions.web_verifications import WebVerify
from page_objects.web.brains_login_page import BrainsLoginPage
from page_objects.web.brains_products_page import BrainsProductsPage
from page_objects.web.brains_cart_page import BrainsCartPage
from page_objects.web.layout_page import *



class BrainsFlows:
    def __init__(self,page:Page):
        self.page = page
        self.login = BrainsLoginPage(page)
        self.products = BrainsProductsPage(page)
        self.footer = BrainsFooter(page)
        self.header = Brainsheader(page)
        self.cart = BrainsCartPage(page)


    

    @allure.step("login:")
    def sign_in(self,email:str,password:str)->None:
        UIActions.update_text(self.login.email_field,email)
        UIActions.update_text(self.login.password_field,password)
        UIActions.click(self.login.login_buttton)



    @allure.step("Get Home Header:")
    def get_home_header(self)->str:
        return UIActions.get_text(self.products.products_heading)
    


    def get_the_numbers_of_products_in_the_cart(self):
        number = UIActions.get_text(self.header.products_in_cart)
        return str(number)


    @allure.step("Add All The Products To The Cart:")
    def add_all_products_to_cart(self)->None:
        total_products = UIActions.count(self.products.add_to_cart_buttons)
        for i in range(total_products):
            UIActions.click(self.products.add_to_cart_buttons.nth(i))
        return total_products
    


    @allure.step("Count the number of products in cart")
    def count_unique_products_in_cart(self):
        UIActions.click(self.header.shopping_cart_icon)
        total_unique_products = UIActions.count(self.cart.products_names)
        print(f"{total_unique_products}")
        return total_unique_products
