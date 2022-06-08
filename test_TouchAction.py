import time

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchAction:
    def setup(self):
        # 关闭w3c验证
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=opt)

        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbottom(self):
        self.driver.get("https://www.baidu.com/")
        el = self.driver.find_element(By.ID, 'kw')
        el_search = self.driver.find_element(By.ID, 'su')
        el.send_keys("test")
        # 通过TouchActions点击“百度一下”
        action = TouchActions(self.driver)
        action.tap(el_search)
        # 滑动到底部
        action.scroll_from_element(el, 0, 10000)
        action.perform()
        time.sleep(3)
        # 点击“下一页”
        nextpage = self.driver.find_element(By.XPATH, '//*[@id="page"]/div/a[10]')
        nextpage.click()
        time.sleep(5)

