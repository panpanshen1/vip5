#函数的定义
# def sum(a,b):
#     print(a+b)
# #函数的调用
# #sum(1,2666)

#函数的定义-有参数有返回值
# def sum(a,b):
#     return a+b
# #有一个sum函数
#
# result = sum (4,9)
# #调用sum函数
# print(result)


# #没有参数，没有返回值
# def sum():
#     print('8888')
# #函数的调用
# sum()


# def sum():
#     return 888

#
# a = int(input('输入数字'))
# b = int(input('输入数字'))
# def sum(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
#     print(a%b)
# sum(a,b)


# a = int(input('输入一个数字'))
# c = input('输入计算方法')
# b = int(input('输入另外一个数字'))
#
# def sum(a,b):
#     print(a+b)
# def max(a,b):
#     print(a*b)
# def min(a,b):
#     print(a/b)
# def m(a,b):
#     print(a-b)
#
#
# if c == '+':
#     sum(a,b)
# elif c == '-':
#     m(a,b)
# elif c == '*':
#     max(a,b)
# elif c == '/':
#     min(a,b)
# else:
#     print('符号不对啊')


# def add(a,b):
#     print(a+b)
# a,b = input('plealse input two value').split(',')
#出来是list，需要加上int进行强制转换
# add(int(a),int(b))
#调用更方便
#函数的定义：求和
# def add(a,b):#形式参数
# #def是关键字，add是函数名，a,b是参数
#     print(a+b)
# #有return是有返回值，没有return是咩有返回值
#
# x,y=input('请输入两个函数，并用逗号隔开:').split(',')
#
#
# #函数的调用
# add(int(x),int(y))#实际参数



# def add(a,b):#形式参数
# #def是关键字，add是函数名，a,b是参数
#     return(a+b)
# #函数的结果在哪里调用，值就会返回哪里
# #有return是有返回值，没有return是咩有返回值
#
# x,y=input('请输入两个函数，并用逗号隔开:').split(',')
#
#
# #函数的调用
# print(add(int(x),int(y)))#实际参数


# def add(a,b):
#     print(a+b)
#     print(a*b)
#     print(a-b)
#     print(a/b)
# x,y=input('请输入两个函数，并用逗号隔开:').split(',')
# #函数的调用
# add(int(x),int(y))
#计算器，实现两个字输入，自动实现加减乘除


# #位置参数
# def sum(a,b):
#     return a+b
# sum(1,2)
#
#
# #默认参数
# def sum(a,b=1):
#     return a+b
#
#
# #可变参数
# def calc(*numbers):
#     print(*numbers)
#     print(numbers)
#     sum=0
#     for n in numbers:
#         sum+=0
#     return sum
# print(calc(1,2))
#
#
# #关键字参数**kwargs
# def person(name,age,**kwargs):
#     print('name',name,'age',age,kwargs)
# person('xiaoming',25,sex='male')

# with open ('','w+') as f:
#     f.write()+'/n'