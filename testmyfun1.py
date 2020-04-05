import unittest
from myfun import *
class testmyfun2(unittest.TestCase):
    def setUp(self):
        print('我是setup')
    def tearDown(self):
        print('我是teardown')
    def testcase1(self):
        result = add(3,4)
        expect = 6
        self.assertEqual(result,expect)
        print(result,'和',expect)
    def testcase2(self):
        result = add(5,4)
        expect = 6
        self.assertEqual(result,expect)
        print(result,'和',expect)
    def testcase3(self):
        result = add(6,4)
        expect = 6
        self.assertEqual(result,expect)
        print(result,'和',expect)


if __name__ == '__main__':
    pass

    #unittest
    '''
    suite = unittest.TestSuite()
    suite.addTest(testmyfun2('testcase2'))
    runner = unittest.TestRunner()
    runner.run(suite)
    '''
    #discover = unittest.defaultTestLoader.discover(r'/Users/shenpanpanpan/Desktop/code/vip5/testmyfun1.py',pattern='test*.py',top_level_dir=None)
    # runner = unittest.TestRunner()
    # runner.run(discover)






