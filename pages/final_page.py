import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Final_page(Base):
    """Работа со страницей Оформления заказа"""


    def __init__(self, driver_g):
        super().__init__(driver_g)
        """Инициализируем атрибуты класса"""
        self.driver = driver_g

    # Locators
    phone_number = "//input[@type='tel']"
    accept_button = "//*[@id='checkout']/div/div[1]/div[2]/div[2]/div[3]/div/button"



    # Getters
    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_accept_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.accept_button)))



    # Actions

    def input_phone_number(self, phonenumber):
        self.get_phone_number().click()
        self.get_phone_number().send_keys(phonenumber)
        print("Input phone number")

    def click_accept_button(self):
        self.get_accept_button().click()
        print("Click accept button")


    # Methods

    def final_checkout(self):
        with allure.step("Final checkout"):
            Logger.add_start_step(method='Final checkout')
            time.sleep(5)
            self.get_current_url()
            self.assert_url("https://www.dns-shop.ru/checkout-main/")
            self.input_phone_number("9991234567")
            self.click_accept_button()
            time.sleep(5)
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method='Final checkout')


        print("---")
