from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import sys
import time


class bcolors:
    status = {True: '\033[92m', False: '\033[91m'}
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class panini():

    def __init__(self, timeout=10, password=None, username=None,
                 driver_path=None):
        '''
        Logs into Paniniamerica.net
        Vars:
            timeout: optional parameter to specify time to wait for webdriver
                to launch
            password: password to login to website
            username: username to login to website
        return:
            N/A, sets self.login value to true or false depending on success
            of website login.
        '''
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        driver = webdriver.Chrome(options=chrome_options,
                                  executable_path=driver_path)

        self.driver = driver
        driver.implicitly_wait(timeout)
        driver.maximize_window()

        driver.get("https://www.paniniamerica.net/login")

        # Website name
        print("{}{}{}".format(bcolors.BOLD, driver.title, bcolors.RESET))

        test = driver.find_elements_by_class_name("form-control")

        # Username Field
        UserLogin = test[5]
        # Password Field
        PassLogin = test[6]
        if username:
            UserLogin.send_keys(username)
        if password:
            PassLogin.send_keys(password)

        login_field = driver.find_elements_by_class_name("filled-btn")

        # Login Button
        output = login_field[1].click()
        status = True
        authenticate_login = driver.find_elements_by_class_name("h-r-points")
        if not (len(authenticate_login) > 0):
            status = False
        print("{}{}Login \t{}{}".format(bcolors.BOLD, bcolors.status[status],
                                        str(status), bcolors.RESET))
        self.login = status

    def trackCards(self, card=None):

        driver = self.driver
        driver.get("https://www.paniniamerica.net/cards.html")
        card_selector = "ce-p-listview"
        card = driver.find_elements_by_xpath(
            "//div[@class='{}']//a[@href='{}']".format(card_selector, card))

        minute = card[0].find_elements_by_xpath(
            "//div[@class='minutes']//div[@class='number']")
        seconds = card[0].find_elements_by_xpath(
            "//div[@class='seconds']//div[@class='number']")
        try:
            while True:
                print('Press any key to stop countdown', end='')
                hour = card[0].find_elements_by_xpath(
                    "//div[@class='hours']//div[@class='number']")
                minute = card[0].find_elements_by_xpath(
                    "//div[@class='minutes']//div[@class='number']")
                seconds = card[0].find_elements_by_xpath(
                    "//div[@class='seconds']//div[@class='number']")
                print("hour", hour[0].get_attribute("innerHTML"),
                      "minute", minute[0].get_attribute("innerHTML"),
                      "second", seconds[0].get_attribute("innerHTML"))
                time.sleep(1)
        except KeyboardInterrupt as e:
            exit()


if __name__ == '__main__':

    args = sys.argv

    username = input("Username: ")
    password = input("Password: ")
    website = panini(username=username, password=password,
                     driver_path="C:\\Users\\jensv\\GitHub\\pythonServer\\"
                     "automation\\chromedriver.exe")
    assert website.login, "Failed to login to website"
    card = input("Card:")
    website.trackCards(card=card)
    # card="/1st-off-the-line-2019-panini-encased-nfl-trading-cards.html")
