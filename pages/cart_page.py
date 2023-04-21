import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Cart_page(Base):
    """Работа со страницей Корзина"""


    def __init__(self, driver_g):
        super().__init__(driver_g)
        """Инициализируем атрибуты класса"""
        self.driver = driver_g

    # Locators
    product_name_in_cart = "//*[@id='cart-page-new']/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[1]/div[1]/div[3]/div/div[1]"
    product_price_in_cart = "//span[@class='price__current'][position()=1]"
    checkout_button = "//button[@id='buy-btn-main']"


    # Getters
    def get_product_name_in_cart(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.product_name_in_cart)))

    def get_product_price_in_cart(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.product_price_in_cart)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.checkout_button)))


    # Actions

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print("Click checkout button")


    # Methods

    def check_values_and_checkout(self):
        with allure.step("Check values and checkout"):
            Logger.add_start_step(method='Check values and checkout')
            self.get_current_url()
            self.assert_url("https://www.dns-shop.ru/cart/")
            with open("docs/product_name.txt", encoding="utf-8") as f:
                name = f.readlines()
                print(name[0])
                self.assert_word(self.get_product_name_in_cart(), name[0])
            with open("docs/product_price.txt", encoding="utf-8") as f:
                price = f.readlines()
                print(price[0])
                self.assert_word(self.get_product_price_in_cart(), price[0])
            self.get_screenshot()
            self.click_checkout_button()
            Logger.add_end_step(url=self.driver.current_url, method='Check values and checkout')




        print("---")
