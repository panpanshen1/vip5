#集合
# s={3,1,2}
# #集合是无序的，且不重复。用来做去重
# #不能通过下标引用
# s.add(4)
# #添加
# s.remove(4)
# #
# s.discard(5)
# if 3 in s:
#     print('hahha')
# s.clear()
# print(s)


#字典
# dict1 = {'name':'xiaowang','age':3,'adress':'泊头'}
# print(dict1['age'])
# dict1['age']=7
# #给xx重新赋值
#
# print(dict1.keys())
# print(dict1.values())
# print(dict1['age'])




#分支和判断

#if分支
# a = int(input('请输入一个数字：'))
# if a>0:
#     a+=1
# print('a的值是：',a)

#
# a = int(input('请输入一个数字：'))
# if a>0:
#     a+=1
# else:
#     a-=1
# print('a的值是：',a)


# list1=[4,6,7,33,66,55]
#
# a=int(input('请输入一个数字：'))
# if a in list1:
#     a+=1
#     print('happy')
# else:
#     print('sad')
#

# b=int(input('请输入一个数字'))
# if b < 60:
#     print('等级为E')
# elif b>= 90 and b<=100:
#     print('等级为A')
# elif b>=80 and b <90:
#     print('等级为B')
# elif b>=70 and b<80:
#     print('等级为C')
# elif b>=60 and b<70:
#     print('等级为D')
# else:
#     print('成绩无效')
#成绩判断的话如果是批量的成绩，应该怎么解决？

#and链接的两个条件必须同时满足，条件才会成立
#or接的两个条件有一个满足，条件才会成立

#while循环
#打印五次*
#a = 0
# #循环变量
# while a<5:
#     #循环条件
#     print('*')
#     #循环体
#     a+=1
    #循环变化
#
# a = 1
# #计数器
# sum = 0
# #和
# while a<=100 :
#     #循环条件
#     sum = sum +a
#     #循环体
#     a +=1
#     #循环变量的变化
# print(sum)

#for循环
# for i in [1,2,3,4]:
#     print (i)


#continue和break
# continue：停止当前这次循环，继续下次循环
# break：跳出所有循环
# for i in range(1,5):
#     if i == 3:
#         continue
#         print(i)
#     else:
#         print(i)

# i=10
# sum = 1
# while i > 0:
#  sum=i*sum
#  i=i-1
#  print(sum)
#10的阶乘


# a = 0
# while a <= 100:
#     a % 3 == 0
#     print(a)
#     a += 1
# lists = []
# for n in range(1,101):
#     if n % 3 == 0:
#         lists.append(n)
# print(lists)
#
# #求100以内能被3整除的数，并将作为列表输出
#
# list1=[1,2,3,4,3,4,2,5,5,8,9,7]
# list2=[ ]
#
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)
#列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表


# list1 = [ i  for i in range(1,100) if i%2 == 0]
# print(list1)
#
# for i in range(1,100):
#     if i % 2 == 0:
#         list1.append(i)
# print(list1)


# example4 = [[1,2,3],[4,5,6],[7,8,9],[10]]
# # example5 =[]
# # #exmaple5 = [j**2 for i in example4 if len(i)>1 for j in i if j%2 == 0]
# # #print(exmaple5)
# # for i in example4:
# #     if len(i)>1:
# #         for j in i :
# #            if j%2 == 0:
# #                example5.append(j**2)
# #
# # print(example5)\
# 想得到多重嵌套的list中一重嵌套中list长度大于1的list中的数为2的倍数的平方组成的list


from  test1  import dakai1
dakai1.add(1,3)
# if __name__ == '__main__':
#     print('有人执行我了')