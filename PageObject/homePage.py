from Common.basePage import BasePage
from selenium.webdriver.common.keys import Keys


class HomePage(BasePage):
    """华为云主页面"""

    signin_button = ['xpath', '//*[@id="header"]/div/div[2]/div[1]/div/div[2]/ul/li[6]/a']  # 登录按钮
    search = ['xpath', '//*[@id="header-navigation-search-input"]']  # 搜索框
    tes1 = ['xpath', '//*[@id="header"]/div/div[2]/div[1]/div/div[2]/ul/li[1]/form/button/i']  #搜索按钮

    def click_sign_in(self):
        """点击Sign in 按钮，跳转登录页面"""
        self.click(self.signin_button)
        self.my_sleep(5)

    def search_for(self, value):
        """输入selenium，并回车"""
        handle1=self.get_handle()
        self.type(self.search, value)
        self.click(self.tes1)
        self.chage_handle(handle1)
