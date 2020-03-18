# for i in [1,2,3,4]:
# #     print(i)


# for i in  range(1,5):
#     if i == 3:
#         break
#         print(i)
#     else:
#         print(i)

# n=1
# sum=1
# while n < 10:
#     sum = sum * n
#     n += 1
# print(sum)

#python 中列表推导式用于使用其他列表创建一个新的列表
#其基本形式【表达式for变量in列表】
# list1=[i for i in range(1,6)]
# # print(list1)

# list1=[i**2 for i in range(1,11)]
# #想得到1-10的平方组成的list
# print(list1)


# #得到1-10中为偶数的平方组成的list
# list1=[i**2 for i in range(1,11) if i %2==0]
# print(list1)


# 想得到多重嵌套中的数是2的倍数的平方组成的list
# example2 = [[1,2,3],[4,5,6],[7,8,9],[10]]
# example3 = [j**2 for i in example2 for j in i if j%2 == 0]
# print(example3)

# example4 = [[1,2,3],[4,5,6],[7,8,9],[10]]
#
# list1 = [  j**2 for  i  in  example4 if len(i) > 1 for j in i if  j % 2 == 0]
#  list1=[j**2 for i  in example4 if len(i)> 0 for j in i if j %2 == 0]
# # # 想得到多重嵌套的list中一重嵌套中list长度大于1的list中的数为2的倍数的平方组成的list
# # list1 =[j**2 for i in example4 if len(i)>1 for j in i if j%2==0]
# # print(list1)
#
# list1 = [j for j in range(1,101) if j % 2==0 and j %3 == 0]
# print(list1)
# #列出100以内偶数中能整除3的所有数字

# list1 = [i for i in range (1,101) if i %3 == 0]
# print(list1)
#求100以内能被3整除的数，并将作为列表输出



# list2 = [1,2,3,4,3,4,2,5,5,8,9,7]
# #列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表
# # print(list1)
# # list1=[]
# # for i in list2:
# #     if i not in list1:
# #         list1.append(i)
# # print(list1)


# #1,1,2,3,5,8,13
# i = 0
# sum = 1
# list1=[0]
# while i <10:
#     list1.append(sum)
#     sum=i+sum
#     i=sum-i
# print(list1)
# #求斐波那契数列 1 1 2 3 5 8 13 ……


#只能被1和它本省整除,质数
# list1=[]
# for i in range(2,101):
#     flg = True
#     for j in range(2 ,i):
#         if i % j  == 0:
#能被除1和本身之外的内容整除
#             flg=False
#这个是false
#             break
#     if flg == True:
#         list1.append(i)
# print(list1)

# a = 3
# a*= 2*3
# print(a)
#18

# example2 = [[1,2,3],[4,5,6],[7,8,9],[10]]
# list1 = [j**2 for i in example2 if len(i)> 1 for j in i if j %2 == 0]
# # list1=[]
# # for i in example2:
# #     if len(i)>1:
# #         for j in i :
# #             if j %2 == 0:
# #                 list1.append(j**2)
# print(list1)
#

#函数的定义
# def add():
#     print('d')
# add()




# def add(a,b):
#     #形式参数
#
#     return a+b
#
# a,b = input('shuru laingeg shuzu ').split(',')
# print(add(a,b))
# #实际参数


# a,b  = input('请输入一个函数').split(',')
# def sum(a,b):
#     print(int(a)+int(b))
# sum(a,b)

# a , b , c= input('输入')
# def add(a,b,c):
#     if c == '-':
#         return (int(a)-int(b))
#     elif  c == '+':
#         return (int(a)+int(b))
#     elif  c == '*':
#         return (int(a)*int(b))
#     elif  c == '/':
#         return (int(a)/int(b))
#     else:
#         return('cde guha')
#
# print(add(a,b,c))


# def sum(a,b=1):
#     return a + b
# print(sum(3))
#默认参数，必选参数在前，默认参数在后，默认参数必须指向不变对象



# def add(l=[]):
#     l.append('end')
#     return l
#
# print(add())
# print(add())
#定义默认参数要牢记一点：默认参数必须指向不变对象，可变对象会变化


# def add(l=None):
#None就是不可变对象
#     if l is None:
#         l=[]
#     l.append('end')
#     return l
# print(add())
# print(add())




#可变参数，可以接受一个或多个参数
# def calc(*numbers):
#     #形参带✳️，就是可变参数，可以接受一个/多个参数
#     print(*numbers)
#     print(numbers)
#     sum = 0
#     for n in numbers:
#         sum +=n
#     return sum
# print(calc(1,2))
#(1,2)元组
#不知道参数多少，大小，但是知道一定是元组/列表


# def  calc(*numbers):
#     print(*numbers)
#     print(numbers)
#     sum = 0
#     for i in  numbers:
#         sum += i
#     return sum
# num=[1,2,4,5,6]
#
# print(calc(*num))



# def person(name,age,**kwargs):
#     print('name',name,'age',age,kwargs)
#
# dicr1 = {'sec':'name','dd':'sd'}
# person('xjag',12,**dicr1)
# #可以传入字典
# #扩展函数的功能，
# #和可变参数类似，也可以先组装一个dict，然后把dict穿进去
#


# a,b = input('shurulaingeshu').split(',')
# def calc(a,b):
#     try:
#
#         print(a/b)
#     except (TypeError,NameError )as result:
#把错误信息打印出来
#         print('nudo')
#         print(type(result))
#
# calc(a,b)
#
#
# a,b = input('susnfdsf').split(',')
# def calc(a,b):
#     try:
#         print(int(a)/int(b))
#     except (BaseException ,NameError) as  result :
#         print(result)
#         print(type(result))
#     finally:
#         print('程序结束')
# calc(a,b)


#BaseException 所有异常的基类
#SystemExit 解释器请求退出
#Keyboardinterrupt  用户中断执行（通常是尖号c）
#Exception 常规错误的基类
# Stoplteration 迭代器没有更多的值
# GeneratorExit 生成器发生异常来通知退出
# BaseException 所有异常的基类
# SystemExit 解释器请求退出
# KeyboardInterrupt 用户中断执行(通常是输入^C)
# Exception 常规错误的基类
# StopIteration 迭代器没有更多的值
# GeneratorExit 生成器(generator)发生异常来通知退出
# StandardError 所有的内建标准异常的基类
# ArithmeticError 所有数值计算错误的基类
# FloatingPointError 浮点计算错误
# OverflowError 数值运算超出最大限制
# ZeroDivisionError 除(或取模)零 (所有数据类型)
# AssertionError 断言语句失败
# AttributeError 对象没有这个属性
# EOFError 没有内建输入,到达EOF 标记
# EnvironmentError 操作系统错误的基类
# IOError 输入/输出操作失败
# OSError 操作系统错误
# WindowsError 系统调用失败
# ImportError 导入模块/对象失败
# LookupError 无效数据查询的基类
# IndexError 序列中没有此索引(index)
# KeyError 映射中没有这个键
# MemoryError 内存溢出错误(对于Python 解释器不是致命的)
# NameError 未声明/初始化对象 (没有属性)
# UnboundLocalError 访问未初始化的本地变量
# ReferenceError 弱引用(Weak reference)试图访问已经垃圾回收了的对象
# RuntimeError 一般的运行时错误
# NotImplementedError 尚未实现的方法
# SyntaxError Python 语法错误
# IndentationError 缩进错误
# TabError Tab 和空格混用
# SystemError 一般的解释器系统错误
# TypeError 对类型无效的操作
# ValueError 传入无效的参数
# UnicodeError Unicode 相关的错误
# UnicodeDecodeError Unicode 解码时的错误
# UnicodeEncodeError Unicode 编码时错误
# UnicodeTranslateError Unicode 转换时错误
# Warning 警告的基类
# DeprecationWarning 关于被弃用的特征的警告
# FutureWarning 关于构造将来语义会有改变的警告
# OverflowWarning 旧的关于自动提升为长整型(long)的警告
# PendingDeprecationWarning 关于特性将会被废弃的警告
# RuntimeWarning 可疑的运行时行为(runtime behavior)的警告
# SyntaxWarning 可疑的语法的警告
# UserWarning 用户代码生成的警告

