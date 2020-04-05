import unittest
import myfile
from myfile import *
class testMyfun(unittest.TestCase):
    def setUp(self):
        print('我是setup')
    def tearDown(self):
        print('我是teardown')
    def testAdd(self):
        result  = add(1,2)
        expect  =  3
        self.assertEqual(result,expect)
        print(expect ,'=',result )
    def testAdd1(self):
        result  = add(1,2)
        expect  =  4
        self.assertEqual(result,expect)
        print(expect ,'=',result )
    @unittest.skip
    def testAdd2(self):
        result  = add(1,2)
        expect  =  5
        self.assertEqual(result,expect)
        print(expect ,'=',result )
    def testAdd3(self):
        result  = add(1,2)
        expect  =  6
        self.assertEqual(result,expect)
        print(expect ,'=',result )

if __name__  ==  '__main__':
    unittest.main()
    #通过创建测试套件的用法
    suite = unittest.TestSuite
    suite.addTest(testMyfun('testAdd'))
    runner = unittest.TestRunner
    runner.run(suite)

    suite = unittest.defaultTestLoader.discover()




