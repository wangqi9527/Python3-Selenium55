from Common.basePage import BasePage


class LoginPage(BasePage):
    """login页面"""

    Username = ['id', 'userNameId']  # 用户名输入框
    Password = ['id', 'pwdId']  # 密码输入框
    Sign_button = ['xpath', '//*[@id="btn_submit"]']  # 登录按钮
    Forgot_password = ['link', 'Forgot password?']  # 忘记密码按钮
    login_error = ['xpath', '//*[@id="checkErrorInfo"]']  # 为空错误提示
    login_error2= ['xpath', '//*[@id="serverError"]/span[1]']

    def login(self, username, password):
        '''登录'''
        self.type(self.Username, username)
        self.type(self.Password, password)
        self.click(self.Sign_button)
        self.my_sleep(5)

    def get_login_error(self):
        """错误提示信息"""
        error_text = self.get_text(self.login_error)
        return error_text

    def get_login_error2(self):
        """错误提示信息2"""
        error_text = self.get_text(self.login_error2)
        return error_text

    def click_forgot_password(self):
        """点击忘记密码按钮"""
        self.click(self.Forgot_password)
