
# #with open('/Users/shenpanpanpan/Desktop/未命名文件夹/第二天/1.txt','r') as f:
# f=open('/Users/shenpanpanpan/Desktop/未命名文件夹/第二天/1.txt','r')
# print(f.read())

# list1 = []
# i = 0
# while i < 100:
#     i +=1
#     if i % 3 == 0:
#         list1.append(i)
# print(list1)
#求100以内能被3整除的数，并将作为列表输出



# sum = 1
# i = 1
# #定义循环变量
# while i <  10 :
#     #循环条件
#     sum=i*sum
#     #乘积是XX，循环体
#     i +=1
#     #循环变量的变化
# print(sum)
# #求10的阶乘


# list1=[1,2,3,4,3,4,2,5,5,8,9,7]
# list2=[]
#
# for i in list1:#循环体
#     if i not in list2:#循环条件
#         list2.append(i)
# print(list2)
#列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表


# i = 0
# sum = 1
# list1=[]
# while i < 10:
#     list1.append(sum)
#     sum=i+sum
#     i=sum-i
# print(list1)
#求斐波那契数列 1 1 2 3 5 8 13 ……



#求100以内的质数（只能被1和它本身整除）
# list1=[]
# for i in range(1,100):
#     for j in range(2,i):
#         if i % j == 0 and i is not j :
#             list1.append(i)
# print(list1)
# list2=[]
# for a in range(2,100):
#     if a not in list1:
#         list2.append(a)
# print(list2)



# with open('/Users/shenpanpanpan/Desktop/未命名文件夹/第二天/1.txt','r')as f:
#     a=f.read()
#     #获取文件的全部内容
#     f.seek(0)
#     d=f.read(9)
#     #读取指定长度字节的数据
#     print(a,d)
#     f.seek(0)
#     b=f.readlines()
#     print(b)
# list1=[]
# for i in b:
#     m = i.strip('\n')
#     list1.append(m)
# print(list1)


##读取以下文件的全部内容，并将所有的数字去重后，放入一个列表
# with open('/Users/shenpanpanpan/Desktop/未命名文件夹/第二天/2.txt','r') as f:
#     a = f.readlines()
#     print(a)
#     # 打印所有行
# list1=[]
# for i in a:
#     m=i.strip('\n')
#     #去掉反斜杠
#     list1.append(m)
#     #放入一个新的列表
# print(list1)
# #打印刚刚的新列表
# i = 0
# #定义循环变量是i
# list2=[]
# list3=[]
# list4=[]
# while i < len(list1):
# #当i的长度比列表1的长度短时进行下面的循环
#    list2=list1[i].split(',')
#    #列表用，元素分割开，命名为新的列表
#    j = 0
#    #定义循环变量是j
#    while j < len(list2):
#        # 当i的长度比列表2的长度短时进行下面的循环
#        list3 = list2[j].split(',')
#        #列表用，元素分割开，命名为新的列表
#        print(list3)
#        k = 0
#        #定义一个循环变量是0
#        list4.append(int(list3[k]))
#        #把刚刚列表的元素们都拿出来组成新的列表
#        k+=1
#        #变量的变化
#        j += 1
#        #变量的变化
#   # print(list2)
#    i += 1
#   #变量的变化
# list5=[]
# print(list4)
# for n in list4:
#     #循环变量
#     if n not in list5:
#         #循环挑条件
#         list5.append(n)
#         #循环体
# print(list5)
#
#
# #print(list1[1].split(','))
#
# # b = list1[0]
# # print(type(b))
# # print(b)
# #
# # list3 = b.split(",")
# # print(list3[2])
#
#
#
#
#     # while j < len(list1[j].split(',')):
#     #     print((list1[i].split(','))[j].split(','))
#     #           j +=1
#
#
#
#
# # j = 0
# # for
# # list2.append()
#
# # str=['1', '2', '3']
# # for i in str:
# #     int(i)
# #     print(i)
#




with open('/Users/shenpanpanpan/Desktop/未命名文件夹/第二天/2.txt','r') as f:
    a = f.readlines()
    print(a)
    # 打印所有行
list1=[]
for i in a:
    m=i.strip('\n')
    #去掉反斜杠
    list1.append(m)
    #放入一个新的列表
print(list1)
#打印刚刚的新列表
i = 0
#定义循环变量是i
list2=[]
list3=[]
list4=[]
while i < len(list1):
#当i的长度比列表1的长度短时进行下面的循环
   list2=list1[i].split(',')
   #列表用，元素分割开，命名为新的列表
   j = 0
   #定义循环变量是j
   while j < len(list2):
       # 当i的长度比列表2的长度短时进行下面的循环
       list3 = list2[j].split(',')
       #列表用，元素分割开，命名为新的列表
       print(list3)
       k = 0
       #定义一个循环变量是0
       list4.append(int(list3[k]))
       #把刚刚列表的元素们都拿出来组成新的列表
       k+=1
       #变量的变化
       j += 1
       #变量的变化
  # print(list2)
   i += 1
  #变量的变化
print(list4)
print(sorted(list4))
d=sorted(list4)
print(d)
with open('/Users/shenpanpanpan/Desktop/未命名文件夹/第二天/3.txt','a') as f1:
       #a是有的时候增加，咩有的时候新建
    for b in d:
        print(b)
        f1.write(str(b)+'\r\n')
           #写入b并且加上空行

       #写入这个







