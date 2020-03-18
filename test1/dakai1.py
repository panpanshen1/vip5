# f = open ('/Users/shenpanpanpan/Desktop/未命名文件夹/第二天/1.txt','r')
# print(f.read())
# f.seek(0)
# print(f.readline())
# f.seek(0)
# print(f.readlines())



# f = open('/Users/shenpanpanpan/Desktop/未命名文件夹/第二天/1.txt','w+')
# # # f.write('hello,word')
# # # print(f.seek(0))
# # # print(f.read())


# with open('/Users/shenpanpanpan/Desktop/未命名文件夹/第二天/1.txt','r') as file:
#     row1 = file.readline()
#     #print(row1)
#     row2=file.readlines()
#     #print(row2)
# list1=[]
# for i in row2:
#     m = i.strip('\n')
#     #去除一些字符串，空格，斜杠n都可以去掉
#     list1.append(m)
# print(list1)

def add():
    print('ddsd')
add()
if __name__ == '__main__':
    print('有人执行我了')
    print(__file__.__doc__)
