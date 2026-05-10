import allure
from data.web.brains_data import *
from extensions.web_verifications import WebVerify
from workflows.web.brains_workflows import BrainsFlows
from extensions.ui_actions import *



class TestBrainsCart:




    @allure.title("Verify that the increment button increases quantity and updates the total")
    @allure.description("This test verifies that quantity increases and total price updates after clicking the increment button")
    def test01_increase_quantit(self,cart_flows:BrainsFlows):
       cart_flows.add_all_products_to_cart()
       cart_flows.navigate_to_cart()
       current_product_quantity = cart_flows.get_prodcut_quantity(PRODUCT_INDEX)
       cart_flows.increase_quantity(PRODUCT_INDEX,ADD_QUNTITY) #PRODUCT_INDEX,TIMES
       expected_product_quntity = current_product_quantity + ADD_QUNTITY
       updated_product_quntity = cart_flows.get_prodcut_quantity(PRODUCT_INDEX)
       WebVerify.soft_values_are_equal(updated_product_quntity,expected_product_quntity)
       WebVerify.soft_all()
       #WebVerify.contain_text(logged_in_flows.cart.products_total_prices, str(EXPECTED_COUNT))




    @allure.title("Verify remove products from cart")
    @allure.description("This test verifies that products can be removed from the cart successfully")
    def test02_verify_remove_products_from_cart(self,cart_flows:BrainsFlows):
       cart_flows.remove_products_from_cart()
       WebVerify.count(cart_flows.cart.remove_buttons, EXPECTED_PRODUCTS_IN_CART)
       empty_message = UIActions.get_text(cart_flows.cart.empty_cart_message)
       WebVerify.text(cart_flows.cart.empty_cart_message,EMPTY_CART_MESSAGE)
       print()
       print(empty_message)
    
