# a = input('提示信息：')
# a,b=input('请输入：').split(',')
# print(type(a))

# a =1
# b= 2
# print('a的值为%s,b的值为%s'%(a,b))
#百分号连接，格式化一一对应，字符串
#数字类型%d
#float类型%f


# a = 1
# b = 2
# print('sad%04d,b的值是%.6f'%(a,b))
# #sad0001,b的值是2.000000
# print('sfds%32d,dsakjfdk%.6f'%(a,b))
# #sfds                               1,dsakjfdk2.000000
# print('safds{},{}'.format(4,6))
# #format都可以的
# print(f'a的值为,{b}')
# #a的值为，2
#
# s1=(1,2.5,'much')
# #不能更新，不能新增
# s2=[1,2.5,'much']
# s3=[1,3,45,2,5,9,3,2,5]
# #增删改都可以
# print(3)
#
# #整体引用
# print(s2)
#
#
# #下标引用
# print(s2[2])
#
# #下限，上限和步长
# print(s3[1:7:2])
# #[3, 2, 9]
#
#
# #特殊引用
# print(s3[-4])[3, 2, 9]


# tuple1 = (1,2,3,4,5,6,7,8,9)
# #定义一个从1到9的元组
# print(tuple1[-3])
# #打印倒数第三个元素
# print(tuple1[3:8:2])
# #打印468



# print(list(range(0,100)))
# #产生一个0到n-1的一个列表


# print(list(range(4,8,2)))
# #产生一个n到m-1的一个列表,步长是2


# print(list(range(0,1000,2)))
# #0到1000的偶数成列表


# list1 = [3,5,6,33,4,9,7,4,2,4543,1332,5766]
# list2=[3,5,63,'5','wrewqtr']
# list1.reverse()
# #逆序排放，改变原来列表的值，原来的列表没有了
# print(list1)

# #list1.sort()
# #排序排放，改变原来列表的值，原来的列表没有了
# print(sorted(list1))
# #没有更改原来的列表
# print(list1)

# list1.insert(4,9)
# #在某一位置(s[4]前面)插入该值9，4为下标
# print(list1)
# list1.insert(6,999)
# list1.insert(5,9986)
# print(list1)

# list1.append(454)
# #列表最后加
# print(list1)

#list2.extend(list1)
#列表1追加到列表2后面

# print(list1.pop(1))
#删除列表的下标为1的
#list1.remove(4)
#删除指定元素第一次出现的值

#print(list1.count(4))
#4元素在里面出现了几个

#print(max(list1))
#列表的最大值
#del list1[1]

# print(list1.index(4))
#获取元素在列表中的下标



# list1.clear()
#清空

# if 4 in list1:
#     print('dsf')
# print(list1)

# l=[11,13,5,7,0,56,23,34,72]
# l1=[66,67,68]
# print(max(l))
# print(min(l))
# print(l.index(56))
# l.append(7)
# print(len(l))
# l.remove(0)
# l.sort()
# print(l)
# l.extend(l1)
# print(l)





# s={3,1,2}
# s.add(3777)
# #向集合s添加元素
#
# #s.remove(3788)
# s.remove(3777)
# #删除集合中的元素，不存在则报异常
#
#
# s.discard(39)
# #删除集合中的元素39，不存在则不报异常
#
#
# s.clear()
# #清空集合
# print(s)



# s={'a':10,'b':20,'c':15}
# print(s.keys())
# #取出所有的key
# print(s.values())
# #取出所有的values
# s['c']=0
# #新增/修改
#
# print(s)
# print(list(s.items()))
#取出所有的键值对，作为一个元组内的元素



# j = {3,4,5,75,4,2,2,1,5,6}
# z = {'a':3,'b':4,'c':6,'d':8}
#
# j.add(55)
# print(j)
#
# z['d']=55
# print(z)
#
# j.remove(3)
# del z['d']
# print(z)
# print(j)
# # list1=list(j)
# # list2=list(z.values())
# # list1.extend(list2)
# list(j).extend(list(z.values()))
# print(list(j))


# list1 = [1,3,4,5,3,2,6]
# num=int(input('输入一个数字'))
# if num in list1:
#     print('happu')

# list1 = [1,3,4,5,3,2,6]
# num=int(input('输入一个数字'))
# if num in list1:
#     print('hanppeu')
#     n=list1.index(num)
#取元素的下标
#     list1[n]+=1
#列表的下标取元素，然后元素加1
#     print(list1)
# #2-	if-else练习—从键盘输入一个数，判断该数是否在列表中，如果在就打印happy，并且让列表中的该值+1，否则打印sad
# else:
#     print('sad')


#循环
# n = 0
# while n < 5:
#     print('#')
#     n+=1

# sum = 0
# n  =  1
# while n < 101:
#     sum = n + sum
#     print(sum)
#     n += 1

# a=6
# a*=3+3
# print(a)



