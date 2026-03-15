from playwright.sync_api import Locator, expect
from smart_assertions import soft_assert, verify_expectations
import allure
from data.web.brains_data import *
from extensions.ui_actions import UIActions
from page_objects.web.brains_login_page import BrainsLoginPage
from page_objects.web.brains_products_page import BrainsProductsPage



class WebVerify:


    @staticmethod
    @allure.step("Verify that the element has text")
    def text(element: Locator, expected_text: str):
        """
        Verifies that the text of the element matches the expected text.
        """
        expect(element).to_have_text(expected_text)



    @staticmethod
    @allure.step("Verify String")
    def strings_are_equal(actual:str,expected:str,message=None):
        assert actual == expected,message



    @staticmethod
    @allure.step("Verify that the element is visible")
    def visible(element: Locator):
        """
        Verifies that the element is visible.
        """
        expect(element).to_be_visible()
    


    @staticmethod
    @allure.step("Verify that the element is not visible")
    def not_visible(element: Locator):
        """
        Verifies that the element is not visible.
        """
        expect(element).not_to_be_visible()
    


    @staticmethod
    @allure.step("Verifies that the number of elements matching the locator is equal to the expected count")
    def count(element: Locator, count: int):
        """
        Verifies that the number of elements matching the locator is equal to the expected count.
        """
        expect(element).to_have_count(count)



    @staticmethod
    @allure.step("Verify that the element contains the expected text")
    def contain_text(element: Locator, expected_text: str):
        """
        Verifies that the text of the element contains the expected text.
        """
        expect(element).to_contain_text(expected_text)



    @staticmethod
    @allure.step("Verify that the element has the expected value")
    def value(element: Locator, expected_value: str):
        """
        Verifies that the value of the element matches the expected value.
        """
        expect(element).to_have_value(expected_value)



    @staticmethod
    @allure.step("Soft assertion to check if the element has the expected text")
    def soft_text(element: Locator, expected_text: str, message: str):
        """
        Soft assertion to check if the element has the expected text.
        Test execution will continue even if this assertion fails.
        """
        actual_text = element.inner_text()
        soft_assert(actual_text == expected_text, message)



    @staticmethod
    @allure.step("Soft assertion to check if the element is visible")
    def soft_is_visible(element: Locator, message: str):
        """
        Soft assertion to check if the element is visible.
        Test execution will continue even if this assertion fails.
        """
        soft_assert(element.is_visible(), message)



    @staticmethod
    @allure.step("Raises all collected assertion errors at once")
    def soft_all():
        """Raises all collected assertion errors at once."""
        verify_expectations()



    @staticmethod
    @allure.step("Soft assert that the list is sorted from high to low")
    def soft_list_sorted_high_to_low(actual_list: list[float], message: str = None):
        for i in range(len(actual_list) - 1):
            soft_assert(
                actual_list[i] >= actual_list[i + 1],
                message or f"Item at index {i} ({actual_list[i]}) is smaller than next item ({actual_list[i+1]})"
            )
        verify_expectations()

    @staticmethod
    @allure.step("Soft assert two values are equals")
    def soft_values_are_equal(actual:int,expected:int,message:str=None):
        soft_assert(actual==expected,message)


    @staticmethod
    @allure.step("Verify href is valid")
    def href_is_valid(element: Locator, expected_href: str = None):
        href = element.evaluate("el => el.getAttribute('href')") or ""
        soft_assert(href != "#" and href != "")
        if expected_href:
            soft_assert(href == expected_href)



    @staticmethod
    def verify_login_error(login:BrainsLoginPage,error_type:str):
        if error_type == "email":
            email_error_message = login.email_field.evaluate("el => el.validationMessage")
            assert email_error_message != ""
        else:
            WebVerify.visible(login.password_error_field)




    @staticmethod
    @allure.step("login with ddt:")
    def verify_ddt_flow(expected_status,error_type:str,products:BrainsProductsPage,login:BrainsLoginPage)->None: 
        if expected_status == "success":
            WebVerify.text(products.products_heading,EXPECTED_HOME_HEADER)
        else:
            WebVerify.verify_login_error(login,error_type)


    
    @staticmethod
    @allure.step("verify the cart status")
    def verify_cart_status(text:str,numer_of_products:int=0):
        if text.isdigit(): 
            expected_count = str(numer_of_products)
            with allure.step(f"Verify cart badge shows {expected_count} products"):
                WebVerify.strings_are_equal(text, expected_count)
        else:
            with allure.step("Verify empty cart message is displayed"):
                WebVerify.strings_are_equal(text, EMPTY_CART_MESSAGE)