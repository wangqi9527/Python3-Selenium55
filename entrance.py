# -*- coding:utf-8 -*-
import os
import unittest
import HTMLTestRunnerCN

import getcwd
from Common.sentMail import sent_mail
from TestSuites.testHome import TestHome
from TestSuites.testLoginOA import TestLogin
from Logs.log import log1

#自动添加指定目录下的所有匹配文件名为XXX开头的文件
test_dir='./TestSuites2/'
pattern='test*.py'
discover= unittest.defaultTestLoader.discover(test_dir,pattern)

if __name__ == "__main__":
    #添加部分测试用例
    #suite = unittest.TestSuite()
    #suite.addTest(TestHome('test_select_selenium'))
    #suite.addTest(TestHome('test_switch_login'))
    #suite.addTest(TestLogin('test_login1'))
    #suite.addTest(TestLogin('test_login2'))
    #suite.addTest(TestLogin('test_login3'))
    #suite.addTest(TestLogin('test_login4'))

    log1.info('加载测试用例')
    path = getcwd.get_cwd()
    file_path = os.path.join(path, 'Report/兰州电网PC端部分功能自动化测试报告.html')
    try:
        fp = open(file_path, 'wb')
        runner = HTMLTestRunnerCN.HTMLTestReportCN(
            stream=fp,
            title='兰州电网PC端部分功能自动化测试报告',
            description='报告描述',
            tester='测试-王琪'
        )
        runner.run(discover)
        log1.info('test end')
        fp.close()
        log1.info('测试报告生成成功')
    except BaseException:
        log1.error("测试报告生成失败", exc_info=1)
    sent_mail()
