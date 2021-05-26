from page.loginPage import LoginPage
from time import sleep
from common import Common


class TestLogin():
    def test_login(self):
        page=LoginPage(Common.driver)
        page.open(Common.url)
        page.password_clear()
        page.name_clear()
        page.name_input("test1")
        page.password_input("123123")
        sleep(1)
        page.login()
        sleep(5)
        result = page.is_exist()
        assert result