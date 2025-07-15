import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    # LOCATORS

    price_cart = '//span[@class="Price_price__AvEcv"]'
    order = '//span[@class="OrderInfo_checkoutButtonResponsive__iPQmV"]'

    # GETTERS
    def get_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_cart)))

    def get_order(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.order)))

    # ACTIONS

    def select_get_order(self):
        self.get_order().click()
        print('Enter order')

    # METHODS
    def select_price_cart(self):
        self.get_current_url()
        self.assert_word(self.get_price(), '109 999 ₽')
        self.select_get_order()
