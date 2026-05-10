
import allure
from extensions.db_actions import DBActions
from extensions.web_verifications import WebVerify
from workflows.web.brains_workflows import BrainsFlows


class TestDB:

    @allure.title("Test - Product Names")
    @allure.description("Verify product names between DB and UI")
    def test01_verify_db(self,logged_in_flows:BrainsFlows,db:DBActions):
      db_items = db.get_products()
      db_product_names = [item[1] for item in db_items]
      ui_product_names=logged_in_flows.get_products_names()
      WebVerify.strings_are_equal(sorted(db_product_names),sorted(ui_product_names))

    
     
