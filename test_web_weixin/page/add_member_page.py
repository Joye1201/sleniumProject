import time

from selenium.webdriver.common.by import By
from test_web_weixin.page.base_page import BasePage
from test_web_weixin.page.contacts_page import ContactsPage


class AddMemberPage(BasePage):
    _location_username = (By.ID, 'username')
    _location_Add_acctid = (By.ID, 'memberAdd_acctid')
    _location_Add_phone = (By.ID, 'memberAdd_phone')
    _location_error_message = (By.CSS_SELECTOR, '.ww_inputWithTips_tips')

    def add_member(self, name, accid, phone):
        """
        添加成员操作
        :return:
        """
        self.find(self._location_username).send_keys(name)
        self.find(self._location_Add_acctid).send_keys(accid)
        self.find(self._location_Add_phone).send_keys(phone)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        return ContactsPage(self.driver)

    def add_member_fail(self, accid, phone):
        """
        添加成员失败操作
        :return:
        """
        self.find(self._location_username).send_keys("盖子")
        self.find(self._location_Add_acctid).send_keys(accid)
        self.find(self._location_Add_phone).send_keys(phone)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

        accid_error = self.finds(self._location_error_message)
        time.sleep(3)
        error_message = [tip.text for tip in accid_error]
        print(error_message)
        return error_message
