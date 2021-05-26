from page.loginPage import LoginPage
from page.homePage import HomePage
from page.custormerAddPage import CustormerAdd
from time import sleep
from common import Common
import pytest


class TestAddCustorner():
    num1=0
    num2=0
    @pytest.fixture(scope="module",autouse=True)
    def login(self):
        page=LoginPage(Common.driver)
        page.open(Common.url)
        page.password_clear()
        page.name_clear()
        page.name_input("test1")
        page.password_input("123123")
        sleep(1)
        page.login()
        sleep(3)
    def test_openBasic(self):
        page=HomePage(Common.driver)
        page.clickBasicManagement()
        page.clickCustormerManagement()
        num1=page.getRows('/html/body/section/section/main/div[2]/div[2]/div/div[2]/div[2]/div/span[1]')
        page.addButton()
    def test_addCustormer(self):
        page=CustormerAdd(Common.driver)
        sleep(3)
        page.legelRepresentative('测试A')
        page.bankAccount('123456789009876')
        page.openAccount('中国银行')
        page.socialCreditCode('123456789')
        page.companyName('自动化测试')
        page.province()
        page.city()
        page.area()
        page.people('带阿达')
        page.department('测试')
        page.phoneNumber('15315560987')
        page.password('123123')
        page.references()
        sleep(1)
        page.clickPicture(file='C:\\Users\\Sxj\\Desktop\\1.jpg')
        page.clickContract(file='C:\\Users\\Sxj\\Desktop\\2.pdf')
        sleep(8)
        page.determine()

