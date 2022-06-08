import time
from selenium.webdriver.common.by import By
from test_web_weixin.page.base_page import BasePage


class ContactsPage(BasePage):
    _location_mem_list = (By.CSS_SELECTOR, '#member_list td:nth-child(2)')
    _location_goto_add_member = (By.CSS_SELECTOR, '.ww_operationBar .js_add_member')
    _location_goto_add_department = (By.CSS_SELECTOR, '.js_create_party')
    _location_add_click = (By.CSS_SELECTOR, '.member_colLeft_top_addBtn')
    _location_dep_list = (By.CSS_SELECTOR, '.jstree-anchor')

    def goto_add_member(self):
        # 解决循环导入问题
        from test_web_weixin.page.add_member_page import AddMemberPage
        """
        跳转到添加成员页面
        :return:
        """
        self.wait_click(self._location_goto_add_member)
        self.find(self._location_goto_add_member).click()
        return AddMemberPage(self.driver)

    def get_member(self):
        """
        获取成员列表，用来做断言信息
        :return:
        """
        time.sleep(3)
        mem_list = self.finds(self._location_mem_list)
        # 列表推导式，获取WebElement对象列表中的文字信息
        member_list = [mem.text for mem in mem_list]
        # for i in mem_list:
        #     member_list.append(i.text)
        print(member_list)
        return member_list

    def goto_add_department(self):
        # 解决循环导入问题
        from test_web_weixin.page.add_department_page import AddDepartmentPage
        """
        跳转到添加部门页面
        :return:
        """
        self.find(self._location_add_click).click()
        self.find(self._location_goto_add_department).click()
        return AddDepartmentPage(self.driver)

    def get_department(self):
        """
        获取部门列表，用来做断言信息
        :return:
        """
        time.sleep(3)
        dep_list = self.finds(self._location_dep_list)
        department_list = [dep.text for dep in dep_list]
        print(department_list)
        return department_list
