# class Cat(object):
#     def  eat(self,chi):
#         print('小猫爱',chi)
#     def  drink(self,he):
#         print('小猫爱',he)
# a = Cat()
# a.eat('吃鱼')
# a.drink('喝水')
#


# class Person(object):
#     def __init__(self,name,weight):
#         self.name = name
#         self.weight = weight
#         print(self.name,'体重',self.weight,'公斤')
#
#     def run(self,paobu):
#         print(self.name,'爱',paobu)
#         print('每次',paobu,'会减肥0.5公斤')
#     def eat(self,dongxi):
#         print(self.name,'爱',dongxi)
#         print('每次',dongxi,'会增加1公斤')
#
# a=Person('小明','45')
# a.run('跑步')
# a.eat('吃东西')
# b=Person('小美','45')
# class Person1(Person):
#     def __init__(self,name,weight):
#         self.name = name
#         self.weight = weight
#         print(self.name,'的体重是',self.weight)
# def calc(temp):
#     temp.__



# class Furniture(object):
#     def __init__(self,area,name):
#         self.area = area
#         self.name = name
#     def chuang(self):
#         print(self.name,'占',self.area)
#     def yigui(self):
#         print(self.name,'占',self.area)
#     def desk(self):
#         print(self.name,'占',self.area)
# class House(object):
#     def __init__(self,type,zarea,list1):
#         self.type = type
#         self.zarea = zarea
#         self.list1 = list1
#     def a(self):
#         print(self.type,self.zarea,self.list1)
# # def  temp(b):
# #
# #     b.a()
#
# cal = Furniture('dd','sdd')
# cal.chuang()
# cal.yigui()



# class Furniture(object):
#     def __init__(self,area):
#         self.area = area
#     def chuang(self,**kwargs):
#         print(kwargs)
# class House(Furniture):
#     def __init__(self,type,zarea):
#         self.type = type
#         self.zarea = zarea
#     def a(self):
#         print(self.type,self.zarea,self)

# b= Furniture('15平米')
# extra ={'床':'2平米','衣柜':'2平米','餐桌':'1.5平米'}
# b.chuang(**extra)
# a = House('一室一厅','10平米')
# a.a()


#房子：户型，总面积，家具名称，搬东西
#家具：名字，占地面积

#类：房子，
#属性：一室一厅，总面积100平米
#方法：搬
#对象：家具
# class Furniture(object):
#     def chuang(self,name,area):
#         print(name,'占',area)
#     def yigui(self,name,area):
#         print(name,'占',area)
#     def desk(self,name,area):
#         print(name,'占',area)
# class House(Furniture):
#     def __init__(self, type, zarea):
#         self.type = type
#         self.zarea = zarea
#     def ban(self,shengyu):
#         print(self.type, '总占地',self.zarea,'剩余',shengyu)
#         Furniture().chuang('床','4')
#         Furniture().yigui('衣柜', '2')
#         Furniture().desk('书桌', '1.5')
#
# #类：家具Furniture.chuang('床','4')
# #属性
# #方法
# #对象
#
#
# a = House('一室一厅','100')
# a.ban('55')



#类：士兵
#属性name
#方法：开火
# class Solider(object):
#     def __init__(self,name):
#         self.name = name
#     def  kaihuo(self):
#         print(self.name,'可以开火')
# class Gun(object):
#     def __init__(self,name):
#         self.name = name
#     def fashe(self):
#         print(self.name,'可以发射子弹')
#     def chuangtian(self):
#         print(self.name,'装填子弹')
#
# class D(Solider,Gun):
#     def a(self):
#         Gun('ak47').chuangtian()
#         Gun('ak47').fashe()
#         Solider('ruien').kaihuo()
# ad=D(Solider)
# ad1 = D(Gun)
# ad.a()

#类：枪
#属性：名字
#方法：发射，装填

