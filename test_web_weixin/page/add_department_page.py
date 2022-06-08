from selenium.webdriver.common.by import By

from test_web_weixin.page.base_page import BasePage
from test_web_weixin.page.contacts_page import ContactsPage


class AddDepartmentPage(BasePage):
    _location_department = (By.CSS_SELECTOR, '.form .qui_inputText.ww_inputText')
    _location_goto_select_department = (By.CSS_SELECTOR, '.js_toggle_party_list')
    _location_select_department = (By.CSS_SELECTOR, '.form .jstree-anchor')
    _location_submit = (By.CSS_SELECTOR, '.ww_dialog_foot .ww_btn_Blue')

    def add_department(self):
        """
        添加部门操作
        :return:
        """
        self.find(self._location_department).send_keys("手机")
        self.find(self._location_goto_select_department).click()
        self.find(self._location_select_department).click()

        self.find(self._location_submit).click()
        return ContactsPage(self.driver)
