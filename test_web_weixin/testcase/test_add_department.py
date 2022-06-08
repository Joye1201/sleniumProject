from test_web_weixin.page.main_page import MainPage


class TestAddDepartment:

    def setup_class(self):
        self.main = MainPage()

    def test_add_department(self):
        """
        添加部门测试用例
        :return:
        """
        dep_list = self.main.goto_contacts().goto_add_department().add_department().get_department()
        assert "手机" in dep_list

    def teardown_class(self):
        self.main.quit()
