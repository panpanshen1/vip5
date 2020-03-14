#类：相同的特性，属性，集合;调用
#方法：动态，动词
#属性：特性
#实例/对象：类中某一个具体的对象或实例
#实例化：从类中找出对象的过程
# class Person(object):
#     #属性为空
#     def eat(self,food):
#         print('吃',food)
#     def sleep(self):
#         print('睡觉')
# a = Person()
# #实例化
#
# #调用类的方法
# a.eat('米饭')


# class Animal(object):
# # 类名
#     #属性
#     name = '夏末'
#     age  = '67'
#     height = '176'
#     #f方法
#     def  eat(self):
#         print(self.name,'吃面条')
#     #打印self的name
#     def sleep(self):
#         print('睡觉')
#
# a = Animal()
# #实例化：变量等于类名
# a.eat()
# a.sex='女'
# #加属性，改属性
# a.sex='男'
# #属性是啥
# print(a.name + a.sex)
# #调用类的方法：对象名.方法名()

# class Student(object):
#     #定义类是学生
#     #属性
#     #方法
#     def study(self,name,xueke):
#         print(name,'学习',xueke)
# a = Student()
# a.study(name='小明',xueke='数学')


# class Student(object):
#     #定义类是学生
#     name = '小明'
#     xuehao = '1234567'
#     #属性
#     def study(self,xueke):
#         #xueke是方法内的参数
#         print('学号是'+self.xuehao+'的学生，学习'+xueke)
# a = Student()
# a.study('数学')
#

# class Student(object):
#     #定义类
#     #属性
#     name = '小明'
#     xuehao = '1234567'
#     def study(self,xueke):
#         print('学号是为{}的学生{}学习{}课程'.format(self.xuehao,self.name,xueke))
# a = Student()
# a.study('数学')


# class  Student(object):
#     xuehao = '123455'
#     name   = '丹姐'
#     xueke = '数学'
#     def study(self):
#         print("学号为%s的学生学习%s课程" % (self.xuehao,self.xueke))
# a = Student()
# a.xuehao = '123'
# a.xueke = '数学'
# a.study()


#init方法不写也会自动调用(实例化的时候自动调用)
#如果类中有init方法，则实例话的时候要根据init方法中的参数来决定是否含参
#init方法中的参数都需要初始化
# class Person(object):
#     aa = 'ss'
#     #公共属性
#     def __init__(self,name,age):
#         #方法会被调用，初始化方法，创建一个实例，创建一个实例的时候，想叫啥就叫啥
#         print('创建了一个实例')
#         self.name = name
#         self.age  = age
#         #实例属性，对象属性
#     def eat(self,food):
#
#         print('名字是',self.name,'吃',food)
# class Teacher(Person):
#     def __init__(self,name,age,gh):
#         #子类继承父类的属性时，必须要加上父类的属性
#         Person.__init__(self,name,age)
#         self.gh =  gh
#     def  kechen(self,place,salary):
#         print('工号为',self.gh,'的老师在',place,'上班，一个月工资',salary)
#     def  shangban(self,course):
#         print('工号为',self.gh,'的老师教',course)
# t1= Teacher('小明','40','007')
# t1.kechen('国贸',10000)
# t1.shangban('英语')
# t1.eat('米饭')



#类的封装
# class Student(object):
#     def __init__(self,xuehao,kecheng):
#         self.xuehao = xuehao
#         self.kecheng=kecheng
#     def study(self):
#         print('学号是'+self.xuehao+'的学生,学习'+self.kecheng)
# # a = Student('1111','数学')
# # a.study()
# if __name__=='__main__':
#     a = Student('sss','sdfds')
#     a.study()


#类的继承，提高代码的复用性，减少代码量
#第一步：继承谁，类中的括号就写谁
#第二步：继承后，子类就具有父类的所有属性和方法，但是父类不能具备子类的属性和方法


# class Person(object):
#     #属性为空
#     def eat(self,food):
#         print('吃',food)
#     def sleep(self):
#         print('睡觉')
#
# class Teacher(Person):
#     def __init__(self,gh,teach,name,didian,xinchou):
#         self.gh =  gh
#         self.teach = teach
#         self.name = name
#         self.didian = didian
#         self.xinchou = xinchou
#     def  kechen(self):
#         print(self.gh,'为',self.name,'的老师，教',self.teach)
#     def  shangban(self):
#         print(self.gh,'为',self.name,'的老师，在',self.didian,'上班，一月工资',self.xinchou)
#
#     def  chifan(self):
#         print('名字是',self.name,'工号为',self.gh,'的老师',self.eat)
#
#
# w=Teacher('1111','数学','王老师','英国','123444')
# w.kechen()
# w.eat('xiaomi')
# w.shangban()
# w.chifan()



# class Person(object):
#     aa = 'ss'
#     #公共属性
#     def __init__(self,name,age):
#         #方法会被调用，初始化方法，创建一个实例，创建一个实例的时候，想叫啥就叫啥
#         print('创建了一个实例')
#         self.name = name
#         self.age  = age
#         #实例属性，对象属性
#     def eat(self,food):
#         print('名字是',self.name,'吃',food)
# class Teacher(Person):
#     def __init__(self,name,age,gh):
#         #子类继承父类的属性时，必须要加上父类的属性
#         Person.__init__(self,name,age)
#         self.gh =  gh
#     def  kechen(self,place,salary):
#         print('工号为',self.gh,'的老师在',place,'上班，一个月工资',salary)
#     def  shangban(self,course):
#         print('工号为',self.gh,'的老师教',course)
#         self.eat('mifan')
#         #子类调用的父类的方法，给了方法
#     def  eat(self,chi):
#         #重写的方法名字一定要和父类的一样，重写的时候要先看下自己的有没有，没有再去看父类的，父类不能满足自身需要的时候，我们可以重写该父类的方法
#         print('工号为',self.gh,'的老师',self.name,'吃',chi)
# t1= Teacher('小明','40','007')
# t1.kechen('国贸',10000)
# t1.shangban('英语')
# t1.eat('米饭')
# t1.eat('吃大米')
# p1=Person('小明','12')
# p1.eat('火腿肠')

# class Dog(object):
#     def print_self(self):
#         print('大家好，我是xxx')
# class xiaotq(Dog):
#     def print_self(self):
#         print('大家好，我是啸天犬')
# def  introduce(temp):
#     temp.print_self()
# d1 = Dog()
# #d1.print_self('xx')
# d2 = xiaotq()
# introduce(d1)
# introduce(d2)





# #私有方法和私有属性
# class A:
#     def __init__(self):
#         self.num1=100
#         self.__num2=200
#         print(self.__num2,self.num1)
#     def test1(self):
#         print('我是公有方法')
#     def __test2(self):
#         print('我是私有方法')
#     def test3(self):
#         print('我是共有方法0')
#         self.__test2()
#         print(self.num1)
#         print(self.__num2)
# class B(A):
#     def test4(self):
#         self.__test2()
#         #不能调用父类的私有方法
#
# aa = B
# a.test4()

#先去分析要定义的类，属性，方法，对象作为一个参数传递
# class Soldier(object):
#     def __init__(self,name):
#         self.name = name
# class Gun(Soldier):
#     def a(self):

import os

# str1 = 'happy'
# result = str1.capitalize()
# print(result)
#
# print(len(str1))
# print(str1.count('p'))