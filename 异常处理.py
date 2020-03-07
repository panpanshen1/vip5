# def calc(a,b):
#     try:
#         print(a/b)
#     except ZeroDivisionError:
#     #如果被除数是0的话，抛出异常
#         print('被除数不能是0')
# a=int(input('输入一个除数'))
# b=int(input('输入被除数'))
#
# calc(a,b)


# try:
#     print(name)
#     #只打印print
# except NameError:
#     print('未定义')


# def calc(a,b):
#     try:
#         print(a/b)
#     except ZeroDivisionError as result:
#         print(result)
# a,b=input('plealse input two value').split(',')
# calc(int(a),int(b))


# def calc(a,b):
#     #print(a+b)
#     try:
#         print(a/b)
#     except ZeroDivisionError as result:
#         print(result)
#     except KeyboardInterrupt as result1:
#         print(result1)
#     except ValueError as result2:
#         print(result2)
#     else:
#         print('c程序执行完毕。')
# a,b= input('please ').split(',')
# calc(int(a),int(b))


# def calc(a,b):
#     try:
#         print(a/b)
#     except NameError as a:
#         print(a)
#         raise
#     #当是nameeerror的时候，就是捕获然后又抛出来
#     except TypeError as msg:
#         print(msg)
#     else:
#         print('chengxuwanbi')
# a,b= input('please ').split('+')
# calc(int(a),int(b))