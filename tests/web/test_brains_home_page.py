import allure
from data.web.brains_data import *
from extensions.web_verifications import WebVerify
from workflows.web.brains_workflows import BrainsFlows
from extensions.ui_actions import *



class TestBrainsHomePage:



    @allure.title("Verify products are ordered by price high to low")
    @allure.description("Verify the products are sorted from highest to lowest price.")
    def test01_verify_order_by_price_high_to_low(self,logged_in_flows:BrainsFlows):
        prices = logged_in_flows.order_products_by_price_high_to_low()
        WebVerify.soft_list_sorted_high_to_low(prices)



    @allure.title("Verify footer social links")
    @allure.description("Check that all social links in the footer are visible and point to the correct URLs.")
    def test02_verify_footer_social_links(self, logged_in_flows: BrainsFlows):
        for link, expected in zip(logged_in_flows.get_footer_social_links(),FOOTER_SOCIAL_LINKS):
            WebVerify.visible(link)
            WebVerify.href_is_valid(link, expected_href=expected)
        WebVerify.soft_all() 



    @allure.title("Verify adding all products to cart")
    @allure.description("This test verifies you can add all the products to the cart")
    def test03_verify_add_all_products_to_cart(self,logged_in_flows:BrainsFlows): 
        total_products = UIActions.count(logged_in_flows.products.add_to_cart_buttons)
        logged_in_flows.add_all_products_to_cart()
        badge_number = logged_in_flows.get_number_of_products_in_cart()
        WebVerify.strings_are_equal(badge_number,str(total_products))



    @allure.title("Verify number of unique products in the cart")
    @allure.description("This test verifies that the cart badge reflects the number of unique products added to the cart or shows the empty cart message.")
    def test04_verify_number_of_products_in_the_cart(self, logged_in_flows:BrainsFlows):        
        cart_text = logged_in_flows.get_cart_state_text()
        WebVerify.verify_cart_status(cart_text,logged_in_flows.get_number_of_products_in_cart())

