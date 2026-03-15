import time

import allure
from data.web.brains_data import *
from extensions.web_verifications import WebVerify
from workflows.web.brains_workflows import BrainsFlows
from extensions.ui_actions import *


class TestCheckoutPage:

    @allure.title("Successful Checkout Flow")
    @allure.description("Verifies completing checkout shows a success message")
    def test_verify_full_checkout_process(self,add_products_flows:BrainsFlows):
        add_products_flows.Checkout_flow(FIRSTNAME,LASTNAME,ZIP_CODE)
        WebVerify.text(add_products_flows.Checkout.checkout_Success_message,EXPECTED_MESSAGE_ORDER)
       
          


        
