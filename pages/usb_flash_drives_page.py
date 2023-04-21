import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class USB_flash_drives_page(Base):
    """Работа со страницей USB Флешки"""


    def __init__(self, driver_g):
        super().__init__(driver_g)
        """Инициализируем атрибуты класса"""
        self.driver = driver_g

    # Locators
    price_max = "//input[@placeholder='до 12 999']"
    title_price = "//span[contains(text(), 'Цена')]"
    price_window = "//div[@data-id='price'][position()=1]"
    brand_window = "//div[@data-id='brand'][position()=1]"
    kingston_check_box = "/ html / body / div[2] / div / div[2] / div[1] / div / div[3] / div[1] / div[5] / div / div / div[2] / label[4]"
    case_design_button = "//div[@data-id='f[5dd]']"
    monolith_with_cap_check_box = "/html/body/div[2]/div/div[2]/div[1]/div/div[3]/div[1]/div[10]/div/div/div/label[4]"
    filters_submit_button = "//button[@data-role='filters-submit']"
    selected_product = "/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[18]/a"
    selected_product_buy_button = "/html/body/div[2]/div/div[2]/div[2]/div[2]/div/div[1]/div[18]/a//following::button[contains(text(), 'Купить')]"



    # Getters
    def get_price_max(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, self.price_max)))

    def get_price_window(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.price_window)))

    def get_brand_window(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.brand_window)))

    def get_kingston_check_box(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.kingston_check_box)))

    def get_case_design_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.case_design_button)))

    def get_monolith_with_cap_check_box(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.monolith_with_cap_check_box)))

    def get_filters_submit_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.filters_submit_button)))

    def get_selected_product(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.selected_product)))

    def get_selected_product_buy_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.selected_product_buy_button)))



    # Actions
    def input_price_max(self, price):
        self.get_price_max().send_keys(price)
        print("Input max price")

    def click_kingston_check_box(self):
        self.get_kingston_check_box().click()
        print("Click kingston check box")

    def click_case_design_button(self):
        self.get_case_design_button().click()
        print("Click case design button")

    def click_monolith_with_cap_check_box(self):
        self.get_monolith_with_cap_check_box().click()
        print("Click monolith with cap check box")

    def click_filters_submit_button(self):
        self.get_filters_submit_button().click()
        print("Click filters submit button")

    def click_selected_product(self):
        self.get_selected_product().click()
        print("Click selected product")

    def click_selected_product_buy_button(self):
        self.get_selected_product_buy_button().click()
        print("Click selected product buy button")


    # Methods

    def select_filters(self):
        with allure.step("Select filters"):
            Logger.add_start_step(method='Select filters')
            self.get_current_url()
            self.assert_url("https://www.dns-shop.ru/catalog/ce3bebe8448b4e77/usb-flash/?virtual_category_uid=fee8309e20e5484a")
            action = ActionChains(self.driver)
            action.move_to_element(self.get_price_window()).perform()
            self.input_price_max("7000")
            action.move_to_element(self.get_brand_window()).perform()
            self.click_kingston_check_box()
            action.move_to_element(self.get_case_design_button()).perform()
            self.click_case_design_button()
            action.move_to_element(self.get_case_design_button()).perform()
            self.click_monolith_with_cap_check_box()
            action.move_to_element(self.get_filters_submit_button()).perform()
            self.click_filters_submit_button()
            self.get_current_url()
            self.assert_url("https://www.dns-shop.ru/catalog/ce3bebe8448b4e77/usb-flash/?price=299-7000&brand=kingston&f%5B5dd%5D=1rm8")
            action.move_to_element(self.get_selected_product()).perform()
            self.click_selected_product_buy_button()
            self.click_selected_product()
            print("---")
            Logger.add_end_step(url=self.driver.current_url, method='Select filters')



