import time

import pytest
from selenium.webdriver.common.by import By
from Base import Base


class TestJs(Base):
    @pytest.mark.skip
    def test_js_scrollbottom(self):
        '''
        案例一：滑到浏览器底部或顶部
        1.打开百度首页
        2.输入搜索关键字
        3.点击搜索后，跳转到搜索结果页
        4.滑动到底部点击“下一页”
        :return:
        '''
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID, 'kw').send_keys("selenium")
        self.driver.execute_script("document.getElementById('su').click()")
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        self.driver.find_element(By.CSS_SELECTOR, '#page > div > a.n').click()
        time.sleep(20)

        # 获取网页标题和网页性能的相应时间
        print(self.driver.execute_script("return document.title; return JSON.stringify(performance.timing)"))

    def test_js_datetime(self):
        '''
        案例二：时间控件处理
        1.打开网址https://www.12306.cn/index
        2.修改出发日期为2022-06-06
        3.打印出发日期
        4.关闭网址
        :return:
        '''
        self.driver.get("https://www.12306.cn/index")
        # 取消时间控件的readonly属性
        # date_js = "document.getElementById('train_date').removeAttribute('readonly')"
        date_js = "document.getElementById('train_date').readonly=false"
        self.driver.execute_script(date_js)

        # 重新设置时间
        date_value = "document.getElementById('train_date').value='2022-06-06'"
        self.driver.execute_script(date_value)
        time.sleep(1)

        # 打印修改后的出发日期
        print(f"出发日期为："+self.driver.execute_script("return document.getElementById('train_date').value"))
