import allure
from data.web.brains_data import *
from extensions.web_verifications import WebVerify
from workflows.web.brains_workflows import BrainsFlows
from extensions.ui_actions import *


class TestBrainsLoginPage:

    @allure.title("Login")
    @allure.description("This test verify login is successful")
    def test01_verify_login(self,brains_flows:BrainsFlows):
        brains_flows.sign_in(EMAIL,PASSWORD)
        WebVerify.text(brains_flows.products.products_heading,EXPECTED_HOME_HEADER)
        # UIActions.refresh(brainsflows.products.page)
        # WebVerify.text(brainsflows.products.products_heading,EXPECTED_HOME_HEADER)
