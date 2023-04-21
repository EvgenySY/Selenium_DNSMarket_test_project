import time
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.accessories_and_services_page import Accessories_and_services_page
from pages.accessories_for_computers_and_laptops_page import Accessories_for_computers_and_laptops_page
from pages.cart_page import Cart_page
from pages.final_page import Final_page
from pages.main_page import Main_page
from pages.product_page import Product_page
from pages.usb_flash_drives_and_hard_drives_page import USB_flash_drives_and_hard_drives_page
from pages.usb_flash_drives_page import USB_flash_drives_page

@allure.description("Test buy product")
def test_buy_product(set_group):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver_g = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProject\\Resource\\chromedriver.exe', options=options)

    mp = Main_page(driver_g)
    mp.authentication()
    mp.open_catalog()

    ans = Accessories_and_services_page(driver_g)
    ans.select_for_computers_and_laptops()

    acl = Accessories_for_computers_and_laptops_page(driver_g)
    acl.select_usb_flash_drives_and_hard_drives()

    usbfh = USB_flash_drives_and_hard_drives_page(driver_g)
    usbfh.select_usb_flash_drives_and_hard_drives()

    usbfd = USB_flash_drives_page(driver_g)
    usbfd.select_filters()

    pp = Product_page(driver_g)
    pp.product_save_values_and_add_to_cart()

    cp = Cart_page(driver_g)
    cp.check_values_and_checkout()

    fp = Final_page(driver_g)
    fp.final_checkout()

    time.sleep(10)




