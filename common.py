import os

from selenium import webdriver


class Common():
    """
    公共配置
    """
    # 当前文件路径
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # 运行测试用例的目录或文件
    cases_path = os.path.join(BASE_DIR, "test_dir")

    # 报告目录
    REPORT_DIR = BASE_DIR + "/test_report/"

    #参数目录
    #DATA_DIR=BASE_DIR+"\\data\\data.json"

    #url配置
    url="http://train-cabin.dev.thundersdata.com/login"

    #dirver_type
    driver_type="chrome-headless"

    #定义driver
    driver=None
    #driver=webdriver.Chrome()

    # 失败重跑次数
    rerun = "0"

    # 当达到最大失败数，停止执行
    max_fail = "5"