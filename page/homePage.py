from base.base import BasePage
import re
class HomePage(BasePage):
    """
    首页
    """
    #基础管理
    def clickBasicManagement(self):
        self.by_xpath('/html/body/section/section/aside/ul/li[1]/div').click()

    #客户管理
    def clickCustormerManagement(self):
        self.by_xpath('/html/body/section/section/aside/ul/li[1]/ul/li[1]').click()
    #客户管理页面
    #新增按钮
    def addButton(self):
        self.by_xpath('/html/body/section/section/main/div[2]/div[2]/div/button[1]').click()
    #删除按钮
    def deleteButton(self):
        self.by_xpath('/html/body/section/section/main/div[2]/div[2]/div/button[2]').click()
    #获取条数
    def getRows(self,xpath):
        num=re.compile(r'\d+')
        ele_text=self.by_xpath(xpath).text
        ele_num=num.search(ele_text).group()
        return ele_num
