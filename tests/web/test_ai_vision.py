import allure
from playwright.sync_api import Playwright, expect
from data.web.brains_data import *
from workflows.web.ai_flows import AiFlow
from workflows.web.brains_workflows import BrainsFlows
from extensions.ai_verifications import AIVerify

class TestAiAdvanced:


    
    @allure.title("Test01 - Verify Page Title with AI Vision")
    @allure.description("verifies the page title using AI on a screenshot.")
    def test01_verify_title_with_vision(self,brains_flows:BrainsFlows,ai_flows:AiFlow):
        brains_flows.sign_in(EMAIL,PASSWORD)
        AIVerify.ai_verify(ai_flows.verify_title(EXPECTED_TITLE))
