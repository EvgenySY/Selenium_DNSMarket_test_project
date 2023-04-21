import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Accessories_and_services_page(Base):
    """Работа со страницей Аксессуары и услуги"""


    def __init__(self, driver_g):
        super().__init__(driver_g)
        """Инициализируем атрибуты класса"""
        self.driver = driver_g

    # Locators
    title_ans = "/html/body/div[2]/div[1]/h1"
    for_computers_and_laptops = "//span[contains(text(),'Для компьютеров и ноутбуков')]"



    # Getters
    def get_title_ans(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.title_ans)))

    def get_for_computers_and_laptops(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.for_computers_and_laptops)))



    # Actions
    def click_computers_and_laptops(self):
        self.get_for_computers_and_laptops().click()
        print("Click Computers and laptops")



    # Methods

    def select_for_computers_and_laptops(self):
        with allure.step("Select for computers and laptops"):
            Logger.add_start_step(method='Select for computers and laptops')
            self.get_current_url()
            print(self.get_title_ans().text)
            self.assert_word(self.get_title_ans(), "Аксессуары и услуги")
            self.click_computers_and_laptops()
            print("---")
            Logger.add_end_step(url=self.driver.current_url, method='Select for computers and laptops')




