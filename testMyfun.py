import unittest
import myfile
from HTMLTestRunner import  HTMLTestRunner
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





