import os
import time
from telnetlib import EC

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Base import Base


class TestFile(Base):
    # @pytest.mark.skip
    def test_file_upload(self):
        '''
        1.打开百度图片网址：https://image.baidu.com
        2.点击上传按钮
        3.将本地的图片文件上传
        :return:
        '''
        self.driver.get("https://image.baidu.com")
        self.driver.find_element(By.XPATH, '//*[@id="sttb"]/img[1]').click()
        # 通过send_keys把图片文件上传到元素中
        self.driver.find_element(By.ID, 'stfile').send_keys("E:\Projects\PycharmProjects\seleniumProject\img\img1.png")
        time.sleep(3)

    @pytest.mark.skip
    def test_alert(self):
        '''
        1.打开网页https://m.runoob.com/try/try.php?filename=jqueryui-api-droppable
        2.操作窗口右侧页面，将元素1拖拽到元素2
        3.这时候会有一个alert弹框，点击弹框中的’确定‘
        4.再按“点击运行”
        5.关闭网页
        :return:
        '''
        self.driver.get("https://m.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 切换到iframeResult,将元素1拖拽到元素2
        self.driver.switch_to_frame('iframeResult')
        drag = self.driver.find_element(By.ID, 'draggable')
        drop = self.driver.find_element(By.ID, 'droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        time.sleep(1)

        # 切换到alert弹框
        alert = self.driver.switch_to.alert
        # 点击“确定”
        alert.accept()
        time.sleep(1)

        # 切换到默认iframe页面，再按“点击运行”
        self.driver.switch_to_default_content()
        self.driver.find_element(By.ID, 'submitBTN').click()
        time.sleep(3)
