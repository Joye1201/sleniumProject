import time

import pytest

from test_web_weixin.page.main_page import MainPage


class TestAddMember:

    def setup_class(self):
        # 实例变量可以在类的其他方法使用
        self.main = MainPage()

    @pytest.mark.parametrize("name, accid, phone",
                             [("纯净水", "1718", "18714171168")] )
    def test_add_member(self, name, accid, phone):
        """
        添加成员测试用例
        :return:
        """
        # 1.跳转到添加成员页面 2.添加成员 3.自动跳转到通讯录页面
        res = self.main.goto_add_member().add_member(name, accid, phone).get_member()
        assert name in res

    @pytest.mark.parametrize("name, accid, phone",
                             [("九阳", "1808", "18714171808")])
    def test_add_member_by_contacts(self, name, accid, phone):
        """
        通过通讯录页面添加成员测试用例
        :return:
        """
        res = self.main.goto_contacts().goto_add_member().add_member(name, accid, phone).get_member()
        assert name in res

    @pytest.mark.parametrize("accid, phone, expect_res",
                             [("1156", "13210091054", "该帐号已被“本子”占有"),
                              ("1443", "13211561156", "该手机号已被“本子”占有")])
    # 第一次参数化，传入重复的accid，正确的手机号，断言信息
    # 第二次参数化，传入正确的accid，重复的手机号，断言信息
    def test_add_member_fail(self, accid, phone, expect_res):
        """
        添加成员失败测试用例
        :param accid: 账号
        :param phone: 手机号
        :param expect_res: 断言信息
        :return:
        """
        res = self.main.goto_add_member().add_member_fail(accid, phone)
        assert expect_res in res

    # 恢复到首页还原一开始的状态
    def teardown(self):
        self.main.back_main()

    # def teardown_class(self):
    #     self.main.quit()
