import unittest

from Common.basePage import BasePage
from PageObject.homePage import HomePage
from PageObject.loginPage import LoginPage
from Logs.log import log1


class TestLogin(unittest.TestCase):
    """测试登录"""

    @classmethod
    def setUpClass(cls):
        browser = BasePage(cls)
        cls.driver = browser.open_browser()
        home = HomePage(cls.driver)
        home.click_sign_in()

    @classmethod
    def tearDownClass(cls):
        login = LoginPage(cls.driver)
        login.dr_quit()

    def test_login1(self):
        """用户名为空"""
        case_name = '用户为空'
        log1.info("执行测试用例：%s" % case_name)
        login = LoginPage(self.driver)
        login.login(' ', '12324')
        error_text = login.get_login_error()
        try:
            self.assertEqual(error_text, '账号名不能为空。')
            log1.info("测试用例执行成功:%s" % case_name + '\n')
        except AssertionError:
            log1.error("测试用例执行失败:%s" % case_name + '\n')
            raise

    def test_login2(self):
        """密码为空"""
        case_name = '密码为空'
        log1.info("执行测试用例：%s" % case_name)
        login = LoginPage(self.driver)
        login.login('LJDY1077', '')
        error_text = login.get_login_error()
        try:
            self.assertEqual(error_text, '密码不能为空。')
            log1.info("测试用例执行成功:%s" % case_name + '\n')
        except AssertionError:
            log1.error("测试用例执行失败:%s" % case_name + '\n')
            raise

    def test_login3(self):
        """密码不正确"""
        case_name = '密码不正确'
        log1.info("执行测试用例：%s" % case_name)
        login = LoginPage(self.driver)
        login.login('WQ68', '12314')
        error_text = login.get_login_error2()
        try:
            self.assertEqual(error_text, '用户名或密码错误，再输错4次该用户将被锁定15分钟。')
            log1.info("测试用例执行成功:%s" % case_name + '\n')
        except AssertionError:
            log1.error("测试用例执行失败:%s" % case_name + '\n')
            raise

    def test_login4(self):
        """登录成功"""
        # 想要执行成功，需使用GitHub账号和密码
        case_name = '登录成功'
        log1.info("执行测试用例：%s" % case_name)
        login = LoginPage(self.driver)
        login.login('WQ688888', 'qwertyuiop666')
        login_title = login.get_title()
        try:
            self.assertEqual(login_title, '绑定邮箱提醒')
            log1.info("测试用例执行成功:%s" % case_name+'\n')
        except AssertionError:
            log1.error("测试用例执行失败:%s" % case_name+'\n')
            raise
