# coding=utf-8
import os
import time
import logging
import pytest
import click
from common import Common


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

'''
说明：
1、用例创建原则，测试文件名必须以“test”开头，测试函数必须以“test”开头。
2、运行方式：
  > python run_tests.py  (回归模式，生成HTML报告)
  > python run_tests.py -m debug  (调试模式)
'''


def init_env(new_report):
    """
    初始化测试报告目录
    """
    os.mkdir(new_report)
    os.mkdir(new_report + "/image")


@click.command()
@click.option('-m', default=None, help='输入运行模式：run 或 debug.')
def run(m):
    if m is None or m == "run":
        logger.info("回归模式，开始执行✈✈！")
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        Common.NEW_REPORT = os.path.join(Common.REPORT_DIR, now_time)
        #init_env(Common.NEW_REPORT)
        html_report = os.path.join(Common.NEW_REPORT, "report.html")
        xml_report = os.path.join(Common.NEW_REPORT, "junit-xml.xml")
        pytest.main(["-s", "-v", Common.cases_path,
                     "--html=" + html_report,
                     "--junit-xml=" + xml_report,
                     "--self-contained-html",
                     "--maxfail", Common.max_fail,
                     "--reruns", Common.rerun])
        logger.info("运行结束，生成测试报告♥❤！")
    elif m == "debug":
        print("debug模式，开始执行！")
        pytest.main(["-v", "-s", Common.cases_path])
        print("运行结束！！")


if __name__ == '__main__':
    run()
