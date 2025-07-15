import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Login_page(Base):
    url = 'https://samara.rbt.ru/'

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver

    # LOCATORS
    plav_window = '//button[@class="PrimaryButton_button__TkLTD SelectCityPopup_buttonYes__6TCBw"]'
    main_word = '(//h2[@class="MainPage_title__bdscF"])[1]'

    # GETTERS
    def skip_plav_window(self):
        a = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.plav_window)))
        a.click()
    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # METHODS
    def autorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.skip_plav_window()
        self.assert_word(self.get_main_word(), 'Категории')


class product_page():

    def __init__(self, driver):
        self.driver = driver

    def product_enter(self):
        select_product = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@href="/cat/komputery_i_orgtehnika/"]')))
        select_product.click()
        print('Click select product')
