import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestForm:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_form_login(self):
        self.driver.get("https://ceshiren.com/account/sign_in")
        login = self.driver.find_element(By.XPATH, '//*[@id="main"]/header/div/div/div[2]/span/a[2]')
        login.click()

        user = self.driver.find_element(By.ID, 'login-account-name')
        password = self.driver.find_element(By.ID, 'login-account-password')
        user.send_keys("597299793@qq.com")
        password.send_keys("yj123456")

        loginbtn = self.driver.find_element(By.ID, 'login-button')
        loginbtn.click()
        time.sleep(3)
