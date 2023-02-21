from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re


class BasePage():
    """
    基础Page层,封装一些常用方法
    """

    def __init__(self, driver):
        self.driver = driver

    # 打开页面
    def open(self, url):
        self.driver.get(url)

    # id定位
    def by_id(self, id, time=3):
        return WebDriverWait(self.driver, time, 1).until(EC.visibility_of_element_located((By.ID, id)))

    # name定位
    def by_name(self, name, time=3):
        return WebDriverWait(self.driver, time, 1).until(EC.visibility_of_element_located((By.NAME, name)))

    # class定位
    def by_class(self, class_name, time=3):
        return WebDriverWait(self.driver, time, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, class_name)))

    # xpath定位
    def by_xpath(self, xpath, time=3):
        return WebDriverWait(self.driver, time, 1).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    # css定位
    def by_css(self, css, time=3):
        return WebDriverWait(self.driver, time, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))

    # 退出网页
    def close(self):
        self.driver.quit()