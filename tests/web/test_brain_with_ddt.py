import allure
import pytest
from data.web.brains_data import *
from extensions.web_verifications import WebVerify
from utils.common_ops import read_data_from_csv
from workflows.web.brains_workflows import BrainsFlows

import os
LOGIN_DATA_PATH = os.path.join("data", "ddt", "login_data.csv")

class TestBrainsDDT:

    @allure.title("Test - Verify LOGIN with DDT")
    @allure.description("Verify login behavior using multiple data sets from CSV")
    @pytest.mark.parametrize("login_data",read_data_from_csv(LOGIN_DATA_PATH))
    def test_verify_login_ddt(self,brains_flows:BrainsFlows,login_data):
        brains_flows.navigate_to(BRAINS_LOGIN_URL)
        brains_flows.sign_in(login_data["email"],login_data["password"])
        WebVerify.verify_ddt_flow(login_data["expected_status"],login_data["expected_error_type"],brains_flows.products,brains_flows.login)
        brains_flows.logout()
