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



