import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Base import Base


class TestFrame(Base):
    def test_frame(self):
        '''
        1.打开包含frame的web页面
        2.打印”请拖拽我“元素的文本
        3.打印”请点击运行“元素的文本
        :return:
        '''
        self.driver.get("https://m.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 切换到iframeResult
        self.driver.switch_to_frame('iframeResult')
        print(self.driver.find_element(By.ID, 'draggable').text)
        # 切换到默认iframe页面
        self.driver.switch_to_default_content()
        print(self.driver.find_element(By.ID, 'submitBTN').text)

        time.sleep(3)
