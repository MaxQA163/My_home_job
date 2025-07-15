import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.Main_page import Main_page
from base.base_class import Base


class Order_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    # LOCATORS

    number = '//input[@class="MaskInput_input__OqrYF"]'
    email = '//input[@class="Input_input__lvORT"]'
    payment = '(//div[@class="PaymentTypeList_description__i_Pix"])[2]'

    # GETTERS
    def get_number(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.number)))

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_payment(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.payment)))

    # ACTIONS

    def select_get_number(self):
        self.get_number().send_keys('1234567890')
        print('Enter your number')
        time.sleep(2)

    def select_get_email(self):
        self.get_email().send_keys('123@mail.ru')
        print('Enter your email')
        time.sleep(2)

    def select_get_payment(self):
        self.get_payment().click()
        print('Enter your payment')

    # METHODS
    def select_order_cart(self):
        self.get_current_url()
        self.select_get_number()
        self.select_get_email()
        self.scroll_down(500)
        time.sleep(2)
        self.select_get_payment()
        self.scroll_down(500)
        time.sleep(2)
        self.get_screenshot()
        print('Well down test')




