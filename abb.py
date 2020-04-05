from testmyfun1 import *

from HTMLTestRunner import HTMLTestRunner
suite = unittest.TestSuite()
suite.addTest(testmyfun2('testcase2'))


if __name__ == '__main__':
    filename = r'/Users/shenpanpanpan/Desktop/code/vip5/re2.html'
    fp = open(filename , 'wb')
    runner = HTMLTestRunner(
        stream = fp,
        title = '测试报告',
        description = '用例执行情况'

    )
    runner.run(suite)
    fp.close()