from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com")
        self.driver.implicitly_wait(3)

    def teardown(self):
        sleep(5)
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.XPATH, '//*[@title="所有分类"]').click()
        category_name = (By.LINK_TEXT, "霍格沃兹答疑区")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(category_name)
        )
