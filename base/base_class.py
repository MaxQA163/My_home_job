import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    '''Method get current url'''
    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url ' + get_url)

    '''Method assert word'''
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')

    '''Method screenshot'''
    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\MaxPC\\pythonLessons\\My_home_job\\screen\\' + name_screenshot)

    '''Method assert url'''
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value url')

    '''Method scroll down'''
    def scroll_down(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    '''Method scroll up'''
    def scroll_up(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")
