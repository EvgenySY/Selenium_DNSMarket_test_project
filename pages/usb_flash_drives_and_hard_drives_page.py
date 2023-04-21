import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class USB_flash_drives_and_hard_drives_page(Base):
    """Работа со страницей USB Флешки и жесткие диски"""


    def __init__(self, driver_g):
        super().__init__(driver_g)
        """Инициализируем атрибуты класса"""
        self.driver = driver_g

    # Locators
    title_usbfah = "/html/body/div[2]/div[1]/h1"
    usb_flash_drives = "//span[contains(text(),'Флешки USB')]"



    # Getters
    def get_title_usbfah(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.title_usbfah)))

    def get_usb_flash_drives(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.usb_flash_drives)))



    # Actions
    def click_usb_flash_drives(self):
        self.get_usb_flash_drives().click()
        print("Click USB flash drives")



    # Methods

    def select_usb_flash_drives_and_hard_drives(self):
        with allure.step("Select usb flash drives and hard drives"):
            Logger.add_start_step(method='Select usb flash drives and hard drives')
            self.get_current_url()
            print(self.get_title_usbfah().text)
            self.assert_word(self.get_title_usbfah(), "USB Флешки и жесткие диски")
            self.click_usb_flash_drives()
            print("---")
            Logger.add_end_step(url=self.driver.current_url, method='Select usb flash drives and hard drives')




