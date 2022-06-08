import time
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestWeWork:
    @pytest.mark.skip
    # 使用remote复用已有的浏览器
    def test_remote(self):
        # 创建一个选项options
        opt = webdriver.ChromeOptions()
        # 创建一个远程ip端口9222
        opt.debugger_address = "127.0.0.1:9222"
        # 把选项应用到Chrome浏览器中
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(3)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        driver.find_element(By.ID, 'menu_contacts').click()
        time.sleep(3)
        # 获取cookie
        print(driver.get_cookies())

    @pytest.mark.skip
    # 使用cookies登录
    def test_cookie(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'secure': False,
             'value': 'true'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False,
             'value': ''},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851198726237'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970324947204853'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851198726237'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '3048237254'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a277477'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '0996324'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'ZxlT0KYvB1npl2nEjMLhdmNdRk0bSz8OsocaeiD-rAVnVwvulS2K9MkpH4GxLfsY'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1686019747, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'lLBPjhiuOmF-OuG8weo-PQRV59d2Q2kry76QV_tOh--FZ_FOZtoYBKBfdIpWAMuon5X40pcSulFaeUh0d7P5N0yRRjYOERNDOi10qdmLw1EuRM9J6xlbFaLNhBuFl4y9HH758i1s-6Td61RXkoRDnqAupSY9i1qY1UPo5hE8iSWD1B9YP0mpEG-AlKfvEJXNc4oVz9jbvz8X-F1UGp7MTG-Kjh9mwg1sj12H78j6W-gooyQM-PKSrGjOo1ybcrC02cXhPD1JfvGnDbf3Sf-lkQ'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1657081042, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'}]
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame")
        driver.find_element(By.ID, 'menu_contacts').click()
        time.sleep(3)
        driver.quit()

    def test_get_cookie(self):
        opt = webdriver.ChromeOptions()
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(3)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        cookie = driver.get_cookies()
        print(cookie)
        # 将cookie写入data.yaml
        with open('../test_web_weixin/testcase/data.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(cookie, f)

    # 使用序列化cookie的方式进行登录
    def test_login(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
        # 注意：当cookie设置时如果检测到未包含cookie中的域名(.work.weixin.qq.com)时，cookie设置会失效(打开默认域名data:,)
        # 设置cookie前必须先打开目标地址(企业微信官网）
        driver.get("https://work.weixin.qq.com/")
        # 读取data.yaml文件
        with open('../test_web_weixin/testcase/data.yaml', encoding='utf-8') as f:
            yaml_data = yaml.safe_load(f)
        # 将cookie传入driver
        for cookie in yaml_data:
            driver.add_cookie(cookie)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        # 进入通讯录页面
        driver.find_element(By.ID, 'menu_contacts').click()
        # 通过ActionChains进行HTML5页面的操作,点击“添加成员”
        add_contacts = driver.find_element(By.LINK_TEXT, '添加成员')
        action = ActionChains(driver)
        action.click(add_contacts)
        action.perform()

        # 添加成员信息
        username = driver.find_element(By.ID, 'username')
        acctid = driver.find_element(By.ID, 'memberAdd_acctid')
        phone = driver.find_element(By.ID, 'memberAdd_phone')
        save = driver.find_element(By.LINK_TEXT, '保存')

        action1 = ActionChains(driver)
        action1.send_keys_to_element(username, '大包包')
        action1.send_keys_to_element(acctid, '888')
        action1.send_keys_to_element(phone, '17511118888')
        action1.click(save)
        action1.perform()
        time.sleep(3)

        # 获取成员列表
        list1 = driver.find_elements(By.CSS_SELECTOR, '#member_list tr td:nth-child(2)')
        member_list = []
        for i in list1:
            member_list.append(i.text)
        print(member_list)
        # 断言验证添加成员是否在成员列表
        assert "大包包" in member_list

        # 退出浏览器
        driver.quit()
