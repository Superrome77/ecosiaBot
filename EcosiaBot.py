import unittest
import time
import random
import selenium
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
class SeleniumTest():
    def __init__(self):
	    options = webdriver.ChromeOptions()
	    options.add_argument("--start-maximized")
	    options.add_argument('--ignore-certificate-errors')
	    options.add_argument("--mute-audio")
	    self._driver = webdriver.Chrome(os.path.abspath("chromedriver.exe"))
	    self._actions = ActionChains(self._driver)
	    self._driver.set_window_size(1250,1500)
    def search(self):
        try:
            for i in range(200):
                time.sleep(1)
                self._driver.get("https://www.ecosia.org/")
                search = self._driver.find_element_by_tag_name("input")
                search.click()
                search.send_keys("%s" %(i))
                search.send_keys(Keys.ENTER)
                time.sleep(3)
        except:
            pass
if __name__ == "__main__":
    rounds = 0
    t = SeleniumTest()
    t.search()
