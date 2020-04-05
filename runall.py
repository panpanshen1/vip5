import unittest
from HTMLTestRunner import HTMLTestRunner
from testMyfun import testMyfun
suite = unittest.TestSuite
print(suite)
suite.addTest(testMyfun('testAdd'))

if __name__  ==  '__main__':
    #unittest.main()
    # #通过创建测试套件的用法
    # suite = unittest.TestSuite
    # suite.addTest(testMyfun('testAdd'))
    # runner = unittest.TestRunner
    # runner.run(suite)

    # discover = unittest.defaultTestLoader.discover()
    # runner = unittest.TestRunner()
    # runner.run(discover)

    #运行测试用例
    # 1.先定义一个报告名称

    report = '/Users/shenpanpanpan/Desktop/code/vip5/report1.html'
    # 2.打开文件，准备写入
    fp = open(report, 'wb')
    # 实力话测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title='但愿测试报告',
                                           description='测试用例详情')
    runner.run(suite)
    # 关闭
    fp.close()

