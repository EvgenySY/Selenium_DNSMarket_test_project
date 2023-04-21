import datetime


class Base():
    """Инициализируем атрибуты класса"""


    def __init__(self, driver_g):
        """Инициализируем атрибуты класса"""
        self.driver = driver_g

    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url: " + get_url)

    """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        print("Screenshot: " + name_screenshot)
        self.driver.save_screenshot(
            'C:\\Users\\User\\PycharmProject\\Selenium_DNSMarket_test_project\\screen\\' + name_screenshot)







