import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    # LOCATORS

    computers = '(//a[@href="/cat/komputery_i_orgtehnika/noutbuki/"])[1]'
    model_computers = '(//span[@class="Checkbox_marker__cZqri"])[4]'
    price_down = '(//input[@class="IntervalFilter_input__Q6UZA"])[1]'
    price_up = '(//input[@class="IntervalFilter_input__Q6UZA"])[2]'
    type_computers = '(//span[@class="Checkbox_marker__cZqri"])[10]'
    name_computers = '//p[@class="Product_name__COY0E common_notMobileVisible__seisu"]'
    add_cart = '//span[@class="Product_basketText__dDXHw"]'
    cart = '//div[@class="BasketAction_action___uYAO"]'
    price = '//div[@class="Product_price__b7Cg2"]'

    # GETTERS
    def get_category_computers(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.computers)))

    def get_model_computers(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.model_computers)))

    def get_price_down(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_down)))

    def get_price_up(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_up)))

    def get_type_computer(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.type_computers)))

    def get_name_computer(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.name_computers)))

    def get_add_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.add_cart)))

    def price_main_page(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price)))

    def get_enter_cart(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.cart)))

    # ACTIONS


    def refresh_str(self):
        self.driver.refresh()

    def click_category_computers(self):
        self.get_category_computers().click()
        print('Click category computers')

    def click_model_computers(self):
        self.get_model_computers().click()
        print('Click model computer: MSI')

    def click_price_down(self):
        element = self.get_price_down()
        ActionChains(self.driver).double_click(element).perform()
        element.send_keys('109999')
        print('Double click down 109999')

    def click_price_up(self):
        element_2 = self.get_price_up()
        ActionChains(self.driver).double_click(element_2).perform()
        element_2.send_keys('109999')
        print('Double click price up 109999')

    def click_type_computer(self):
        self.get_type_computer().click()
        print('Click type gaming PC')

    def click_add_cart(self):
        self.get_add_cart().click()
        print('Add cart')

    def click_enter_cart(self):
        self.get_enter_cart().click()
        print('Enter cart')

    # METHODS
    def select_category(self):
        self.get_current_url()
        self.scroll_down('300')
        self.click_category_computers()
        self.click_price_down()
        self.click_price_up()
        self.click_model_computers()
        self.scroll_down('1500')
        time.sleep(5)
        self.click_type_computer()
        self.scroll_up('-1500')
        self.refresh_str()
        self.assert_word(self.get_name_computer(), 'Ноутбук игровой MSI Bravo 17 C7VE/9S7-17LN11-044/Ryzen 5 '
                                                   '7535HS/8Gb/SSD256Gb/17.3FHD 144Hz/RTX 4050 6Gb/DOS черный')
        self.click_add_cart()
        time.sleep(5)
        self.click_enter_cart()
