# f = open('/Users/shenpanpanpan/Desktop/未命名文件夹/第二天/1.txt','r')
# print(f.readlines())
# def add():
#     try:
#         f = open('/Users/shenpanpanpan/Desktop/未命名文件夹/第二天/199.txt', 'r')
#         print(f.readlines())
#         f.close()
#     except (BaseException , NameError) as  result:
#
#         print(result)
#         print(type(result))
#     finally:
#         print('程序结束')
#
#
# add()

# f = open('/Users/shenpanpanpan/Desktop/未命名文件夹/第二天/19.txt', 'a')
# m='hello \n dsfd'
# f.writelines(m)

# with open('/Users/shenpanpanpan/Desktop/未命名文件夹/第二天/1.txt', 'r') as f:
#  f.readlines()
#  print(f.readlines())
#



# #模块和包
# import dakai
#
# dakai.fun1()
# #调用模块内部的方法

# from dakai import *
# fun2()
#直接调用


# from test1 import dakai1
# dakai1.add(3,4)

# from dakai import fun1
# fun1()


#具有相同的特性，且能够完成某些动作的事物组成的一个集合
#属性：类中的事物所具有的特性，趋于静态

# class Add(object):
#     def eat(self,food):
#         print('chi',food)
#     def sleep(self):
#         print('ddd')
# a = Add()
# a.eat('mian')
# a.sleep()


# class Person(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age  = age
#     def add(self):
#         print('dfdsf',self.name,self.age)
# a = Person('x',14)
# a.add()


# class  Student(object):
#     def  study(self,name,course):
#         print(name,'学习',course)
# a = Student()
# a.study('xiao','sjus')


# class Student(object):
#     def __init__(self,sno):
#         self.sno=sno
#     def syudy(self,course):
#         print('学号为%s的学生，学习%s课程'%(self.sno,course))
# a=Student('1233')
# a.syudy('shuxe')


# class Teacher(object):
#     def __init__(self,gh):
#         self.gh = gh
#     def teach(self,kemu):
#         print('gh为%s的老师，教%s课程'%(self.gh,kemu))
# a=Teacher('2354')
# a.teach('ying')
#


# class Animal(object):
#     def eat(self):
#         print('-----吃')
#     def drink(self):
#         print('-----喝')
# class Dog(Animal):
#     def bark(self):
#         print('____汪汪叫')
# # class Xiaotq(Dog):
# #     def fly(self):
# #         print('------飞')
# #         Dog.bark(self)
# #         #调用被重写的方法，父类的名字，方法名（）
# #         super().bark()
# def temp(a):
#     a.eat()
# dog1 = Dog()
# dog2=Animal()
# temp(dog1)
# temp(dog2)

# x=Xiaotq()
# x.fly()
# x.bark()


# class Base(object):
#     def test(self):
#         print('sdkfjd')
# class A(Base):
#     def test1(self):
#         print('打印1234')
# class B(Base):
#     def test2(self):
#         print('我是testb')
# class C(A,B):
#     def test3(self):
#         print('dfd')
# a=C()
# a.test()


