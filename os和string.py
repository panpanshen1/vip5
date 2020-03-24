import os,stat
#os.chdir(path)
#改变当前工作目录
#os.getcwd()
# def print_path():
#     print_path(os.getcwd())

import requests
'''
print(os.access('/Users/shenpanpanpan/Desktop/未命名文件夹/第二天/1.txt',os.R_OK))
os.F_OK: 作为access()的mode参数，测试path是否存在。
os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
os.W_OK 包含在access()的mode参数中 ， 测试path是否可写。
os.X_OK 包含在access()的mode参数中 ，测试path是否可执行。

path = '/Users/shenpanpanpan/Desktop/未命名文件夹/第二天/1.txt'
print(os.getcwd())
os.chdir('/Users/shenpanpanpan/Desktop/code/interfaceTestVip5/')
修改目录到
print(os.getcwd())
查看修改后的路径
os.chdir('/Users/shenpanpanpan/Desktop/code/vip5')
print(os.getcwd())
#os.chdir('/Users/shenpanpanpan/Desktop/code/interface')

path = '/Users/shenpanpanpan/Desktop/未命名文件夹/第二天/1.txt'
os.chmod( '/Users/shenpanpanpan/Desktop/未命名文件夹/第二天/1.txt', stat.S_IXGRP)
os.chown('/Users/shenpanpanpan/Desktop/未命名文件夹/第二天/1.txt',100,-1)

os.chroot('/User/)
改变当前的根目录

os.close(fd)
关闭目录

print(os.path.abspath('第二天/1.txt'))
返回绝对路径
print(os.path.basename('/Users/shenpanpanpan/Desktop/未命名文件夹/第二天/1.txt'))
返回文件名
print(os.path.dirname('第二天/1.txt'))
返回文件路径，相对路径

print(os.path.exists('第二天/1.txt'))
路径存在则返回True，路径损坏则返回False

print(os.path.dirname(__file__))

'''