import unittest
import time
import random
import selenium
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

total = 0
class SeleniumTest():
    def __init__(self):
        global total
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--mute-audio")
        self._driver = webdriver.Chrome(os.path.abspath("chromedriver.exe"),chrome_options=options)
        self._actions = ActionChains(self._driver)
        self._driver.set_window_size(1250,1500)
        self.search()
        
    def search(self):
        global total
        roundSearch = 0
        try:
            for i in range(20000):
                self._driver.get("https://www.ecosia.org/")
                time.sleep(1)
                search = self._driver.find_element_by_tag_name("input")
                search.click()
                search.send_keys("%s" %(i))
                search.send_keys(Keys.ENTER)
                time.sleep(1)
                plants = self._driver.find_element_by_xpath("//span[@class='pill-text tree-counter-text js-treecount-text']")
                plantNum = int(plants.text)
                if plantNum > roundSearch:
                    roundSearch = plantNum
                    print("Searches this round = %i" %(roundSearch))
                try:
                    ad = self._driver.find_element_by_xpath("//span[@class='ad-hint js-ad-hint']")
                    self._actions.move_to_element_with_offset(ad,0,-5)
                    self._actions.click()
                    self._actions.perform()
                    self._actions.reset_actions()
                    ad.click()
                except:
                    pass
            total += roundSearch
            print("Total searches = %i" %(total))
            self._driver.close()
        except:
            print("passing")
            total += roundSearch
            print("Total searches = %i" %(total))
            pass


    def totalset(self):
        print("total set")
        self._total = 0
if __name__ == "__main__":
    while True:
        rounds = 0
        t = SeleniumTest()
        t.search()
