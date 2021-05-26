from base.base import BasePage

class CustormerAdd(BasePage):
    """
    客户新增页面
    """
    #法人代表输入框
    def legelRepresentative(self,keys):
        self.by_xpath('/html/body/section/section/main/div[2]/div[2]/form/div[1]/div[2]/div[1]/input').send_keys(keys)
    #银行账号输入框
    def bankAccount(self,keys):
        self.by_xpath('/html/body/section/section/main/div[2]/div[2]/form/div[2]/div[2]/div/input').send_keys(keys)
        #/html/body/section/section/main/div[2]/div[2]/form/div[2]/div[2]/div
    #开户银行输入框
    def openAccount(self,keys):
        self.by_xpath('/html/body/section/section/main/div[2]/div[2]/form/div[3]/div[2]/div[1]/input').send_keys(keys)
    #社会信用代码输入框
    def socialCreditCode(self,keys):
        self.by_xpath('/html/body/section/section/main/div[2]/div[2]/form/div[4]/div[2]/div/input').send_keys(keys)
    #公司名称输入框
    def companyName(self,keys):
        self.by_xpath('/html/body/section/section/main/div[2]/div[2]/form/div[5]/div[2]/div/input').send_keys(keys)
    #单位地址
    #点击选择确认省份
    def province(self):
        self.by_xpath('/html/body/section/section/main/div[2]/div[2]/form/div[6]/div[2]/div[1]/div/div/div/input').click()
        self.by_xpath('/html/body/div/div[1]/div[1]/ul/li[1]').click()
    #点击选择确认城市
    def city(self):
        self.by_xpath('/html/body/section/section/main/div[2]/div[2]/form/div[6]/div[2]/div[2]/div/div/div/input').click()
        self.by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li').click()
    #点击选择确认区
    def area(self):
        self.by_xpath('/html/body/section/section/main/div[2]/div[2]/form/div[6]/div[2]/div[3]/div/div/div[1]/input').click()
        self.by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
    #订舱人输入框
    def people(self,keys):
        self.by_xpath('/html/body/section/section/main/div[2]/div[2]/form/div[8]/div[2]/div/input').send_keys(keys)
    #部门输入框
    def department(self,keys):
        self.by_xpath('/html/body/section/section/main/div[2]/div[2]/form/div[9]/div[2]/div/input').send_keys(keys)
    #手机号输入框
    def phoneNumber(self,keys):
        self.by_xpath('/html/body/section/section/main/div[2]/div[2]/form/div[11]/div[2]/div/input').send_keys(keys)
    #登陆密码输入框
    def password(self,keys):
        self.by_xpath('/html/body/section/section/main/div[2]/div[2]/form/div[14]/div[2]/div/input').send_keys(keys)
    #欧亚班列推荐人
    #点击选择推荐人
    def references(self):
        self.by_xpath('/html/body/section/section/main/div[2]/div[2]/form/div[15]/div[2]/div/div/input').click()
        self.by_xpath('/html/body/div[4]/div[1]/div[1]/ul/li').click()
    #营业执照
    def clickPicture(self,file):
        self.driver.find_element_by_xpath(
            '/html/body/section/section/main/div[2]/div[2]/form/div[17]/div[2]/div/div/input').send_keys(file)
        #self.by_xpath('/html/body/section/section/main/div[2]/div[2]/form/div[17]/div[2]/div/div/input').send_keys(file)
        #/html/body/section/section/main/div[2]/div[2]/form/div[17]/div[2]/div/div/input
    #合同
    def clickContract(self,file):
        self.driver.find_element_by_xpath('/html/body/section/section/main/div[2]/div[2]/form/div[18]/div[2]/div/div/input').send_keys(file)
        #self.by_xpath('/html/body/section/section/main/div[2]/div[2]/form/div[18]/div[2]/div/div/input').send_keys(file)
    #确认按钮
    #点击保存
    def determine(self):
        self.by_xpath('/html/body/section/section/main/div[2]/div[2]/form/div[19]/button[1]').click()
    #重置按钮
    #点击后输入清空
    def reset(self):
        self.by_xpath('/html/body/section/section/main/div[2]/div[2]/form/div[19]/button[2]').click()