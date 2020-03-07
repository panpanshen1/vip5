#
# a = [11,13,5,7,0,56,23,34,72]
#
# print(min(a),max(a),len(a))
# print(a.index(56))
# a.append(7)
# print(a)
# a.pop(4)
# print(a)
# a.sort()
# print(a)
#
#
# b=[66,67,68,0]
# a.extend(b)
# print(a)

# -*- coding:utf-8 -*-
# coding=utf-8
# encoding=utf8
# i = 0
# string = 'ILoveFishC.com'
# while i < len(string):
#     print(i)
#     i += 1

# i = 0
# string = 'ILoveFishC.com'
# length = len(string)
# while i < length:
#     print(i)
#     i += 1

# count = 3
# password = 'FishC.com'
#
# while count:
#     passwd = input('请输入密码：')
#     if passwd == password:
#         print('密码正确，进入程序......')
#         break
#     elif '*' in passwd:
#         print('密码中不能含有"*"号！您还有', count, '次机会！', end=' ')
#         continue
#     else:
#         print('密码输入错误！您还有', count-1, '次机会！', end=' ')
#     count -= 1


# count=3
# password='fishc.com'
# while count:
#     psd = input('请输入密码：')
#     if password == psd :
#         print('密码正确，进入程序......')
#         break
#     elif '*' in psd:
#         print('密码中不能含有"*"号，您还有',count,'次机会')
#         continue
#     else:
#         print('密码输入错误，你还有',count-1,'次机会')
#     count -= 13
#
# import json
# data = {
#     'no':1,
#     'name':'Runoob',
#     'url':'http://www.runoob.com'
# }
#
# json_str=json.dumps(data)
# print('python 原始数据：',repr(data))
# print('json 对象：',json_str)
#
# data1 = json.loads(json_str)
# print("data1['name']:",data1['name'])
# print("data2['url']:",data1['url'])

#
# list_1_10=[x**2 for x in range(1,11) ]
# print(list_1_10)
# # 想得到1-10的平方组成的list
#
# example = [i**2 for i in  range(1,11) if i % 2==0]
# print(example)
# # 想得到1-10中为偶数的平方组成的list
#
# example2=[[1,2,3],[4,5,6],[7,8,9],[10]]
# example3=[j**2 for i in example2  for j in i if j%2==0]
# print(example3)
# # 想得到多重嵌套中的数是2的倍数的平方组成的list
#
# example4 = [[1,2,3],[4,5,6],[7,8,9],[10]]
# exmaple5 = [j**2 for i in example2 if len(i)>1 for j in i if j%2 == 0]
# print(exmaple5)
# # 想得到多重嵌套的list中一重嵌套中list长度大于1的list中的数为2的倍数的平方组成的list
# example = [i for i in range(1,100) if i % 2== 0]
# print(example)
# list_1_100 =[j for j in [i for i in range(1,100) if i % 2== 0] if j%3==0 ]
# print(list_1_100)
#列出100以内偶数中能整除3的所有数字

#
# s={3,1,2}
# s.add(4)
# #向集合s添加元素n
# s.remove(2)
# #删除集合的元素4，如果元素中不存在，报Keyerror异常
# s.discard(0)
# #删除集合的元素4，如果元素中不存在，不报异常
# #s.clear()
# #清空集合
# print(s)

# s={'a':10,'b':20,'c':15}
# #字典
# print(s['c'])
# #通过键来引用
# print(s)
# #整体引用
#
# s.keys()
# #取出所有的键
#
# s.values()
# #取出所有的值
#
# s.items()
# #、取出所有的键值对，作为一个元组内的元素
#
# del s['a']
#
# print(s.values())


dic={'a':10,'b':20,'c':90}
jihe={2,6,3,2,4,9}

jihe.add(55)
#集合加元素
dic['d']=55
#字典加元素
jihe.remove(3)
#集合删除元素
del dic['a']
#字典删元素
# print(jihe)
# print(dic)
c=list(dic.values())
#字典的值列表
d=list(jihe)
#集合的列表
# print(d)
# print(c)
c.extend(d)
#连接两个列表
print(c)



# a=int(input('请输入一个数字'))
# print(a)



# a = [3,5,6,7,3]
# # print(a.append(5))
# # print(a.count(3))
# # print(a.index(7))
# # print(9 in a)