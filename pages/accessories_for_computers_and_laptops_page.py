import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Accessories_for_computers_and_laptops_page(Base):
    """Работа со страницей Аксессуары для компьютеров и ноутбуков"""


    def __init__(self, driver_g):
        super().__init__(driver_g)
        """Инициализируем атрибуты класса"""
        self.driver = driver_g

    # Locators
    title_afcal = "/html/body/div[2]/div[1]/h1"
    usb_flash_drives_and_hard_drives = "//span[contains(text(),'USB Флешки и жесткие диски')]"



    # Getters
    def get_title_afcal(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.title_afcal)))

    def get_usb_flash_drives_and_hard_drives(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.usb_flash_drives_and_hard_drives)))



    # Actions
    def click_usb_flash_drives_and_hard_drives(self):
        self.get_usb_flash_drives_and_hard_drives().click()
        print("Click USB flash drives and hard drives")



    # Methods

    def select_usb_flash_drives_and_hard_drives(self):
        with allure.step("Select usb flash drives and hard drives"):
            Logger.add_start_step(method='Select usb flash drives and hard drives')
            self.get_current_url()
            print(self.get_title_afcal().text)
            self.assert_word(self.get_title_afcal(), "Аксессуары для компьютеров и ноутбуков")
            self.click_usb_flash_drives_and_hard_drives()
            print("---")
            Logger.add_end_step(url=self.driver.current_url, method='Select usb flash drives and hard drives')




