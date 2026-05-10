import os
import time
import uuid
import sqlite3
import pytest
from pytest import FixtureRequest
from playwright.sync_api import Page, Playwright
from data.api.placeholder_posts_data import *
from extensions.db_actions import DBActions
from data.web.brains_data import *
from utils.common_ops import load_config
from utils.fixture_helpers import  get_browser
from workflows.api.placeholder_posts_workflows import PlaceholderPostsApiFlows
from workflows.web.ai_flows import AiFlow
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
    request_context=playwright.request.new_context(base_url=PLACEHOLDER_BASE_URL)
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
    return brains_flows



# Fixture for home page tests (already logged in)
@pytest.fixture(scope="class")
def add_products_flows(brains_flows:BrainsFlows):
    brains_flows.sign_in(EMAIL,PASSWORD)
    brains_flows.add_all_products_to_cart()
    return brains_flows

# Fixture for home page tests (already logged in)
@pytest.fixture(scope="class")
def cart_flows(brains_flows:BrainsFlows):
    brains_flows.sign_in(EMAIL,PASSWORD)
    brains_flows.add_all_products_to_cart()
    brains_flows.navigate_to_cart()
    return brains_flows


@pytest.fixture
def post_flows(request_context):
    return PlaceholderPostsApiFlows(request_context)



@pytest.fixture
def ai_flows(page: Page):
    # כאן page הוא fixture של Playwright
    return AiFlow(page)



@pytest.fixture(scope="class",autouse=True)
def db(request:FixtureRequest):
    db_path = r"data\data_base\items.db"
    my_db = sqlite3.connect(db_path)
    db_actions= DBActions(my_db)
    yield db_actions
    db_actions.close_db()



