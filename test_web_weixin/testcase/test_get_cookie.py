import yaml
from selenium import webdriver


class TestGetCookie:
    def test_get_cookie(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(3)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookie = self.driver.get_cookies()
        with open('cookie_data.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(cookie, f)