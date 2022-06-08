from wework.po.login_page import LoginPage
from wework.po.register_page import RegisterPage


class IndexPage:

    def goto_login(self):
        return LoginPage()

    def goto_register(self):
        return RegisterPage()
