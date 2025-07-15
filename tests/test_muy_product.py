import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

from pages.Cart_page import Cart_page
from pages.Login_page import Login_page
from pages.Main_page import Main_page
from pages.Order_page import Order_page


def test_muy_product():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    print('Start test 1')

    login = Login_page(driver)
    login.autorization()

    select_category_pc = Main_page(driver)
    select_category_pc.select_category()

    price_cart = Cart_page(driver)
    price_cart.select_price_cart()

    last_order = Order_page(driver)
    last_order = last_order.select_order_cart()

