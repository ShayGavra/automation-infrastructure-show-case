import pytest
from pytest import FixtureRequest
from playwright.sync_api import Playwright

# from data.api.chuck_api_data import *
from data.web.brains_data import BRAINS_URL, EMAIL, PASSWORD
from utils.common_ops import load_config
from utils.fixture_helpers import get_browser
# from workflows.api.chuck_api_flows import ChuckApiFlows
from workflows.web.brains_workflows import BrainsFlows

# Load the configuration
CONFIG = load_config()     

@pytest.fixture(scope="class")
def page(playwright: Playwright, request:FixtureRequest):
    browser = get_browser(playwright,CONFIG["BROWSER_TYPE"].lower())
    context = browser.new_context(no_viewport=True)        
    page = context.new_page()
    page.goto(BRAINS_URL)
    yield page    
    # Best practice: Close page before context
    page.close()
    context.close()
    browser.close()

@pytest.fixture(scope= "class")
def request_context(playwright: Playwright, request:FixtureRequest):
    request_context=playwright.request.new_context(base_url=CHUCK_BASE_URL)
    yield request_context
    request_context.dispose()


# Fixture for login tests (negative or positive)
@pytest.fixture(scope="class")
def brains_flows(page):
    return BrainsFlows(page)

# Fixture for home page tests (already logged in)
@pytest.fixture(scope="class")
def logged_in_flows(brains_flows:BrainsFlows):
    brains_flows.sign_in(EMAIL,PASSWORD)
    print(brains_flows.page.url)
    return brains_flows

@pytest.fixture
def chuck_flows(request_context):
    return ChuckApiFlows(request_context)

