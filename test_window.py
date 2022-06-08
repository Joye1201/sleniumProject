import time

import pytest
from selenium.webdriver.common.by import By
from Base import Base


class TestWindow(Base):
    @pytest.mark.skip
    def test_switchwindows(self):
        '''
        1.打开百度首页
        2.点击“登录”
        3.弹框中点击“立即注册”，输入用户名、手机号和密码
        4.返回刚才的登录页
        5.输入用户名和密码，点击登录
        :return:
        '''
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.LINK_TEXT, "登录").click()
        self.driver.find_element(By.LINK_TEXT, "立即注册").click()
        # 获取当前所有窗口的句柄
        handles = self.driver.window_handles
        print(handles)

        # 跳转到“立即注册”页输入用户名、手机号和密码
        self.driver.switch_to.window(handles[-1])
        print(self.driver.current_window_handle)
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__userName').send_keys("gaobaobao0109")
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__phone').send_keys("13012341234")
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__password').send_keys("k12345678")

        # 跳转会“登录”页输入用户名和密码，并点击登录
        self.driver.switch_to.window(handles[0])
        print(self.driver.current_window_handle)
        time.sleep(1)
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__userName').send_keys("gaobaobao0109")
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__password').send_keys("k12345678")
        self.driver.find_element(By.ID, "TANGRAM__PSP_11__submit").click()
        time.sleep(3)

    def test_hogwarts(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element(By.ID, 'kw').send_keys("霍格沃兹测试")
        self.driver.find_element(By.ID, 'su').click()
        time.sleep(20)

        self.driver.find_element(By.PARTIAL_LINK_TEXT, '霍格沃兹测试开发腾讯课堂官网').click()
        # 打印所有窗口句柄
        handles = self.driver.window_handles
        print(handles)
        time.sleep(3)
        
        # 切换到最后一个窗口
        self.driver.switch_to_window(handles[-1])
        # 打印当前窗口句柄
        curhandle = self.driver.current_window_handle
        print(curhandle)
        self.driver.find_element(By.PARTIAL_LINK_TEXT, '高级进阶/Java/测试开发/名企定向培养/软件测试').click()
        time.sleep(3)




