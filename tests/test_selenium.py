#!/usr/bin/env python3

import logging
import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(
    format="%(levelname)-8s %(asctime)s %(filename)s:%(lineno)s] %(message)s",
)
logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)


class TestOrderProcess(unittest.TestCase):

    def setUp(self):
        driver_path = os.getenv("DRIVER_PATH", os.path.join(os.getenv("HOME", ""), "chromedriver"))
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        # options.add_argument("--headless")
        # options.add_argument("--remote-debugging-port=9222")
        self.driver: RemoteWebDriver = webdriver.Chrome(executable_path=driver_path, options=options)

    def test_home_title(self):
        driver = self.driver
        driver.get("https://www.google.de")
        self.assertEqual("Google", driver.title)

    def test_search(self):
        driver = self.driver
        driver.get("https://www.google.de")

        wait = WebDriverWait(driver, 10)
        btn: WebElement = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#L2AGLb")))
        btn.click()

        wait = WebDriverWait(driver, 10)
        search_input: WebElement = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name=\"q\"]")))
        search_input.send_keys("ViUR")
        search_input.send_keys(Keys.ENTER)

        self.assertEqual("ViUR - Google Suche", driver.title)
        # time.sleep(50)


if __name__ == "__main__":
    unittest.main(verbosity=2)
