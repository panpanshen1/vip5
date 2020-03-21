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
#     def chuang(self,name):
#         print(name,'占',self.area)
#     def yigui(self,name,):
#         print(name,'占',self.area)
#     def desk(self,name,):
#         print(name,'占',self.area)
# class House(Furniture):
#     def __init__(self,type,zarea):
#         self.type = type
#         self.zarea = zarea
#     def a(self):
#         print(self.type,self.zarea,self)
# b= Furniture('15平米')
# extra ={'床':'4','衣柜':'2','餐桌':'1.5'}
# c = extra.values()
# sum = 0
# # for i in c:
# #     sum = i+sum
# # print(sum)
# print(c)
# b.chuang(**extra)
# a = House('一室一厅','10')
# b.chuang('床')


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
#     def ban(self):
#         # shengyu = int(self.zarea) -
#         print(self.type, '总占地',self.zarea,'剩余')
#         Furniture().chuang('床','4')
#         Furniture().yigui('衣柜', '2')
#         Furniture().desk('书桌', '1.5')
#
# a = House('一室一厅','100')
#a.ban()
# #类：家具Furniture.chuang('床','4')
# #属性
# #方法
# #对象
#
#




#类：士兵
#属性name
#方法：开火

# class Gun(object):
#     def __init__(self,name):
#         self.name = name
#     def fashe(self):
#         print(self.name,'可以发射子弹')
#     def chuangtian(self):
#         print(self.name,'装填子弹')
#     def have(self):
#         Solider('ruien').have()
#         print('有一把',self.name)
# class Solider(Gun):
#     def __init__(self,name):
#         self.name = name
#     def  kaihuo(self):
#         print(self.name,'可以开火')
#     def have(self):
#         print('士兵',self.name)
# class D(Gun):
#     def a(self):
#         Gun('ak47').chuangtian()
#         Solider('ruien').kaihuo()
#         Gun('ak47').fashe()
#         Gun('ak47').have()
#         #Solider('ruien').have()
#
# ad=D(Solider)
# ad1 = D(Gun)
# ad.a()
## F(ad)
## F(ad1)

#类：枪
#属性：名字
#方法：发射，装填



# 3、摆放家具
# 需求：
# 1）.房子有户型，总面积和家具名称列表
#    新房子没有任何的家具
# 2）.家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平面
#    餐桌：占1.5平米
# 3）.将以上三件家具添加到房子中
# 4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表

'''
#房子类 House
属性：户型apartment  总面积 total_area  家具列表furniture_list  剩余面积 residual_area
方法：添加家具add_furniture


#家具类Furniture
属性：名字name 占地面积cover_area
'''
class House(object):
    def __init__(self, apartment, total_area):
        self.furniture_list = []
        self.apartment = apartment
        self.total_area = total_area
        self.residual_area = self.total_area
    def add_furniture(self, item):
        # 家具名称列表新增家具名称
        print('开始添加家具')
        self.furniture_list.append(item.name)
        # 剩余面积会减少（剩余面积 = 总面积-家具占地面积）
        self.residual_area  = self.residual_area -item.cover_area
        print('添加家具成功')
        pass
    # 返回实例对象的类的描述信息，
    def __str__(self):
        return '创建了一个户型为%s,面积为%s平的房子,剩余面积为%s平,家具有%s的房子' % (self.total_area, self.apartment,self.residual_area,self.furniture_list)
    #py自己的东西，__str__,用return，调用类的时候就会打印出来了
class Furniture(object):
    def __init__(self,name,cover_area):
        self.name = name
        self.cover_area = cover_area
    def __str__(self):
        return '创建了一个%s家具，占地面积为%s'%(self.name,self.cover_area)


h = House('三室一厅',120)
print(h)

f =Furniture('床',4)

h.add_furniture(f)
print(h)


# class strtest:
#     def __init__(self):
#         print("init: this is only test")
#     def __str__(self):
#         return "str: this is only test"
#
# if __name__ == "__main__":
#     st=strtest()
#     print (st)