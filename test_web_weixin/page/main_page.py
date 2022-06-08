import time

from selenium.webdriver.common.by import By

from test_web_weixin.page.add_member_page import AddMemberPage
from test_web_weixin.page.base_page import BasePage
from test_web_weixin.page.contacts_page import ContactsPage


class MainPage(BasePage):
    _location_goto_add_member = (By.CSS_SELECTOR, '.ww_indexImg_AddMember')
    _location_goto_contacts = (By.ID, 'menu_contacts')
    _location_back_main = (By.ID, 'menu_index')
    _location_cancel = (By.CSS_SELECTOR, 'a[node-type="cancel"]')

    def goto_add_member(self):
        """
        跳转到添加成员页面
        :return:
        """
        self.find(self._location_goto_add_member).click()
        return AddMemberPage(self.driver)

    def goto_contacts(self):
        """
        跳转到通讯录页面
        :return:
        """
        time.sleep(1)
        self.find(self._location_goto_contacts).click()
        return ContactsPage(self.driver)

    def back_main(self):
        self.find(self._location_back_main).click()
        # self.find(self._location_cancel).click()
