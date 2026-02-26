import time

import allure
from data.web.brains_data import *
from extensions.web_verifications import WebVerify
from workflows.web.brains_workflows import BrainsFlows
from extensions.ui_actions import *


class TestBrainsHomePage:

    @allure.title("Verify adding all products to cart")
    @allure.description("This test verifies you can add all the products to the cart")
    def test01_verify_add_products_to_cart(self,logged_in_flows:BrainsFlows): 
        logged_in_flows.add_all_products_to_cart()


    @allure.title("Verify number of unique products in the cart")
    @allure.description("This test verifies that the cart badge reflects the number of unique products added to the cart")
    def test02_verify_number_of_products_in_the_cart(self,logged_in_flows:BrainsFlows):
        logged_in_flows.count_unique_products_in_cart()
    



    