import allure
from playwright.sync_api import Page
from data.web.brains_data import *
from extensions.ui_actions import UIActions
from extensions.web_verifications import WebVerify
from page_objects.web.brains_checkout_page import BrainsCheckoutPage
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
        self.Checkout = BrainsCheckoutPage(page)


    
    @allure.step("Navigte to:")
    def navigate_to(self,url:str)->None:
        UIActions.navigate_to(self.page,url)


    @allure.step("Logout from user:")
    def logout(self)->None:
        if UIActions.element_exist(self.products.products_heading):
            UIActions.click(self.header.user_icon)
            UIActions.click(self.header.logout_button)
            UIActions.click(self.header.confirm_logout)




    @allure.step("login:")
    def sign_in(self,email:str,password:str)->None:
        UIActions.update_text(self.login.email_field,email)
        UIActions.update_text(self.login.password_field,password)
        UIActions.click(self.login.login_buttton)



    @allure.step("Get Home Header:")
    def get_home_header(self)->str:
        return UIActions.get_text(self.products.products_heading)
    


    @allure.step("Get the number of products in the cart")
    def get_number_of_products_in_cart(self):
        if UIActions.count(self.header.products_in_cart) > 0:
            return UIActions.get_text(self.header.products_in_cart)
        return 0  





    @allure.step("Add All The Products To The Cart:")
    def add_all_products_to_cart(self)->None:
        total_products = UIActions.count(self.products.add_to_cart_buttons)
        for i in range(total_products):
            UIActions.click(self.products.add_to_cart_buttons.nth(i))
        return total_products
    


    @allure.step("Get cart text or number of products")
    def get_cart_state_text(self):
        """
        מחזיר את הטקסט שמופיע בעגלה:
        - אם יש מוצרים, מחזיר את מספר המוצרים כמחרוזת
        - אם העגלה ריקה, מחזיר את הטקסט שמופיע ב־UI
        """
        UIActions.click(self.header.shopping_cart_icon)

        total_unique_products = UIActions.count(self.cart.products_names)
        
        if total_unique_products > 0:
            # מחזיר את מספר המוצרים בעגלה כמחרוזת
            return str(total_unique_products)
        
        # מחזיר את הטקסט של העגלה הריקה
        return UIActions.get_text(self.cart.empty_cart_message)
    
    

    @allure.step("Order products by price from high to low and get the prices")
    def order_products_by_price_high_to_low(self) -> list[float]:
        UIActions.click(self.products.order_by_button)
        UIActions.click(self.products.order_by_options.last)
        
        prices_text = UIActions.get_all_text(self.products.prices)
        prices = [float(price[1:]) for price in prices_text]  # המרה למספרים
        
        return prices
        


    @allure.step("Get all footer social links")
    def get_footer_social_links(self):
        count = UIActions.count(self.footer.footer_social_links)
        return [self.footer.footer_social_links.nth(i) for i in range(count)]
    

    
    @allure.step("Complete checkout flow")
    def Checkout_flow(self,lastName:str,firstName:str,zip_code:int)->None:
        UIActions.click(self.header.shopping_cart_icon)
        if UIActions.element_exist(self.cart.checkout_button):
            UIActions.click(self.cart.checkout_button)
            UIActions.update_text(self.Checkout.first_name_field,firstName)
            UIActions.update_text(self.Checkout.last_name_field,lastName)
            UIActions.update_text(self.Checkout.zip_code,str(zip_code))
            UIActions.click(self.Checkout.continue_button)
            UIActions.click(self.Checkout.finish_button)
            text_message= UIActions.get_text(self.Checkout.checkout_Success_message)
        else:
            print("Cart is EMPTY!")
        return text_message
    


    def navigate_to_cart(self):
        UIActions.click(self.header.shopping_cart_icon)


    @allure.step("Increase product quantity by a given number and get total")
    def increase_quantity(self,product_index:int,times:int)->int:
        increase_button = self.cart.increase_button.nth(product_index)
        if UIActions.count(increase_button)>0:
            for _ in range(times):
                UIActions.click(increase_button)
     
        

    def get_prodcut_quantity(self,product_index:int)->int:
        return int(UIActions.get_text(self.cart.quantity.nth(product_index)))



    @allure.step("Remove all products from the shopping cart")
    def remove_products_from_cart(self)->int:
        UIActions.click(self.header.shopping_cart_icon)
        removed = 0
        while self.cart.remove_buttons.count() > 0:
            UIActions.click(self.cart.remove_buttons.first)
            UIActions.click(self.cart.confirm_remove_button)
            removed +=1
        return removed
    

