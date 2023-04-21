import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):
    """Работа со страницей аутентификации"""

    url = 'https://www.dns-shop.ru/'

    def __init__(self, driver_g):
        super().__init__(driver_g)
        """Инициализируем атрибуты класса"""
        self.driver = driver_g

    # Locators
    login_icon = "// div[ @class ='user-profile__login']"
    login_button_icon = "//span[contains(text(),'Войти')][position()=1]"
    enter_with_password_button = "//div[contains(text(),'Войти с паролем')]"
    username = "//input[@autocomplete='username']"
    password = "//input[@autocomplete='current-password']"
    login_button = "//button[@class='base-ui-button-v2_big base-ui-button-v2_brand base-ui-button-v2_ico-none base-ui-button-v2']"
    login_icon_1 = "//div[@class='user-profile__container']"
    nickname = "//div[@class='user-profile__username']"
    accessories_and_services = "//a[contains(text(),'Аксессуары и услуги')]"


    # Getters
    def get_login_icon(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.login_icon)))

    def get_login_button_icon(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.login_button_icon)))

    def get_enter_with_password_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.enter_with_password_button)))

    def get_username(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.username)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_login_icon_1(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.login_icon_1)))

    def get_nickname(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.nickname)))

    def get_accessories_and_services(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable((By.XPATH, self.accessories_and_services)))


    # Actions
    def click_login_icon(self):
        self.get_login_icon().click()
        print("Click Login icon")

    def click_login_button_icon(self):
        self.get_login_button_icon().click()
        print("Click Login button under icon")

    def click_enter_with_password_button(self):
        self.get_enter_with_password_button().click()
        print("Click Enter with password button")

    def input_username(self, user_name):
        self.get_username().click()
        self.get_username().send_keys(user_name)
        print("Input username")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click Login button")

    def click_login_icon_1(self):
        self.get_login_icon_1().click()
        print("Click Login icon")

    def click_accessories_and_services(self):
        self.get_accessories_and_services().click()
        print("Click accessories and services")


    # Methods

    def authentication(self):
        with allure.step("Authentication"):
            Logger.add_start_step(method='Authentication')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_login_icon()
            self.click_login_button_icon()
            self.click_enter_with_password_button()
            self.input_username('nijay17971@momoshe.com')
            self.input_password('Pass11word')
            time.sleep(3)
            self.click_login_button()
            self.click_login_icon_1()
            print("Nickname: " + self.get_nickname().text)
            self.assert_word(self.get_nickname(), "Test Testov")
            print("---")
            Logger.add_end_step(url=self.driver.current_url, method='Authentication')

    def open_catalog(self):
        with allure.step("Open catalog"):
            Logger.add_start_step(method='Open catalog')
            self.click_accessories_and_services()
            print("---")
            Logger.add_end_step(url=self.driver.current_url, method='Open catalog')

