import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Product_page(Base):
    """Работа со страницей выбранного товара"""


    def __init__(self, driver_g):
        super().__init__(driver_g)
        """Инициализируем атрибуты класса"""
        self.driver = driver_g

    # Locators
    product_name = "//h1[@class='product-card-top__title']"
    product_price = "//div[@class='product-buy__price']"
    cart_button = "//a[@data-commerce-target='CART']"



    # Getters
    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.product_name)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.product_price)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.cart_button)))


    # Actions

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click cart button")


    # Methods

    def product_save_values_and_add_to_cart(self):
        with allure.step("Product save values and add to cart"):
            Logger.add_start_step(method='Product save values and add to cart')
            self.get_current_url()
            self.assert_url("https://www.dns-shop.ru/product/4f6c6f4802043332/pamat-usb-flash-256-gb-kingston-datatraveler-exodia-dtx256gb/")
            value_product_name = self.get_product_name().text
            with open("docs/product_name.txt", "w", encoding="utf-8") as f:
                f.write(value_product_name)
            print("Product name: " + value_product_name)
            value_product_price = self.get_product_price().text
            with open("docs/product_price.txt", "w", encoding="utf-8") as f:
                f.write(value_product_price)
            print("Product price: " + value_product_price)
            self.click_cart_button()
            print("---")
            Logger.add_end_step(url=self.driver.current_url, method='Product save values and add to cart')


