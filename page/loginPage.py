from base.base import BasePage
class LoginPage(BasePage):
    """
    登录页
    """
    #点击登入
    def login(self):
        self.by_xpath('/html/body/div/div/div/div[2]/button').click()

    #清空用户名输入
    def name_clear(self):
        self.by_id('username').clear()

    #清空密码输入
    def password_clear(self):
        self.by_id('password').clear()

    #输入用户名
    def name_input(self,name):
        self.by_id('username').send_keys(name)

    #输入密码
    def password_input(self,password):
        self.by_id('password').send_keys(password)

    #判断登录是否失败
    def is_exist(self):
        result=True
        try:
            self.by_id('username')
        except:
            result=True
        else:
            result=False
        return result