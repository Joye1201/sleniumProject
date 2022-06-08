import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("https://ceshiren.com/")
        element_click = self.driver.find_element(By.CSS_SELECTOR, '#navigation-bar li:nth-child(3)')
        action = ActionChains(self.driver)
        # 点击“热门”
        action.click(element_click)
        action.perform()
        time.sleep(3)

    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element(By.ID, 's-usersetting-top')
        action = ActionChains(self.driver)
        # 将鼠标移动到“设置”位置
        action.move_to_element(ele)
        action.perform()
        time.sleep(3)

    @pytest.mark.skip
    def test_keys(self):
        self.driver.get("https://www.baidu.com/")
        login = self.driver.find_element(By.ID, 's-top-loginbtn')
        login.click()

        username = self.driver.find_element(By.ID, 'TANGRAM__PSP_11__userName')
        username.click()
        password = self.driver.find_element(By.ID, 'TANGRAM__PSP_11__password')
        password.click()
        submit = self.driver.find_element(By.ID, 'TANGRAM__PSP_11__submit')
        
        action = ActionChains(self.driver)
        # 向用户名中输入内容
        action.send_keys_to_element(username, "yejiao1145").pause(1)
        # 向左删除一格
        action.send_keys(Keys.BACK_SPACE).pause(1)
        # CTRL+A
        action.key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL)
        # 向密码中输入内容
        action.send_keys_to_element(password, "12345678").pause(1)
        action.click(submit)
        action.perform()
        time.sleep(3)

    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        dragme = self.driver.find_element(By.ID, 'dragger')
        Item1 = self.driver.find_element(By.XPATH, '/html/body/div[2]')

        action = ActionChains(self.driver)
        # 将dragme移动到Item1
        action.drag_and_drop(dragme, Item1).perform()
        time.sleep(3)
