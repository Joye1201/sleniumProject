import os
from selenium import webdriver


class Base:
    def setup(self):
        # 配置多浏览器驱动
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'handles':
            self.driver = webdriver.PhantomJS()
        else:
            # executable_path配置环境变量
            self.driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
