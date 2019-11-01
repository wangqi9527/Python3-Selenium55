import unittest
from Common.basePage import BasePage
from PageObject.homePage import HomePage
from Logs.log import log1


class TestHome(unittest.TestCase):
    """测试主页面"""

    def setUp(self):
        browser = BasePage(self)
        self.driver = browser.open_browser()

    def test_select_selenium(self):
        """测试搜索"""
        case_name = '测试搜索'
        log1.info("执行测试用例：%s" % case_name)
        home = HomePage(self.driver)
        home.search_for('安全组')
        home.my_sleep(2)
        title = home.get_title()
        try:
            self.assertEqual(title, '安全组 华为云_搜索结果页')
            log1.info("测试用例执行通过：%s" % case_name+'\n')
        except AssertionError:
            log1.error("测试用例执行失败：%s" % case_name+'\n')
            raise

    def test_switch_login(self):
        """切换到login页面"""
        case_name = '切换至login页面'
        log1.info("执行测试用例：%s" % case_name)
        home = HomePage(self.driver)
        home.click_sign_in()
        home_title = home.get_title()
        try:
            # Sign in中间空格删了，验证失败后会被测试报告统计
            self.assertEqual(home_title, '用户登录—华为云')
            log1.info("测试用例执行通过：%s" % case_name+'\n')
        except AssertionError:
            log1.error("测试用例执行失败：%s" % case_name+'\n')
            raise

    def tearDown(self):
        home = HomePage(self.driver)
        home.dr_quit()
