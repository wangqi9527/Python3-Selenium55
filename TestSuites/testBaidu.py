import unittest
from Common.basePage import BasePage
from PageObject.BaiduPage import BaiduPage
class test_baidu(unittest.TestCase):
    '''百度首页'''

    def setUp(self):
        bro = BasePage(self)
        self.driver = bro.open_browser()

    def test_baisu(self):
        '''测试百度搜索'''
        baisu = BaiduPage(self.driver)
        baisu.type_kw('selenium')
        baisu.click_su()
        baisu.dr_quit()
if __name__ == '__main__':
    unittest.main()