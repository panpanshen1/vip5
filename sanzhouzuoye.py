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

# class House(object):
#     def __init__(self, apartment, total_area):
#         self.furniture_list = []
#         self.apartment = apartment
#         self.total_area = total_area
#         self.residual_area = self.total_area
#     def add_furniture(self, item):
#         # 家具名称列表新增家具名称
#         if self.residual_area < item.cover_area:
#             print('为空了，没了')
#         else:
#             print('开始添加家具')
#             self.furniture_list.append(item.name)
#             # 剩余面积会减少（剩余面积 = 总面积-家具占地面积）
#             self.residual_area  = self.residual_area -item.cover_area
#             print('添加家具成功')
#         pass
#     # 返回实例对象的类的描述信息，
#     def __str__(self):
#         return '创建了一个户型为%s,面积为%s平的房子,剩余面积为%s平,家具有%s的房子' % (self.total_area, self.apartment,self.residual_area,self.furniture_list)
#     #py自己的东西，__str__,用return，调用类的时候就会打印出来了
# class Furniture(object):
#     def __init__(self,name,cover_area):
#         self.name = name
#         self.cover_area = cover_area
#     def __str__(self):
#         return '创建了一个%s家具，占地面积为%s'%(self.name,self.cover_area)
#
#
# h = House('三室一厅',120)
# print(h)
#
# f =Furniture('床',400)
#
# h.add_furniture(f)
# print(h)


# class strtest:
#     def __init__(self):
#         print("init: this is only test")
#     def __str__(self):
#         return "str: this is only test"
#
# if __name__ == "__main__":
#     st=strtest()
#     print (st)


'''
#士兵 Soldier
属性：name  
方法：开火  fire
有  have


#枪 Gun
属性：name
方法：装填 put  发射 Lunch
'''

# class Gun(object):
#     def __init__(self,gunname):
#         self.gunname = gunname
#     # def  put(self):
#     #     print('%s可以装填子弹'%(self.gunname))
#     # def  lunch(self):
#     #     print('%s可以发射子弹' % (self.gunname))
#     def __str__(self):
#         return '%s可以装填子弹,%s可以发射子弹'%(self.gunname,self.gunname)
# class Soldier(object):
#     def __init__(self,name):
#         self.name = name
#     def fire(self):
#         print('士兵可以开火')
#     def __str__(self):
#         return '%s可以装填子弹,%s可以发射子弹' % (self.gunname, self.gunname)
#
# g = Gun('ak47')
# print(g)
# s=Soldier('sd')
# print(s)

#coding:utf-8

#
# 4.士兵开枪
# 需求：
# 1）.士兵瑞恩有一把AK47
# 2）.士兵可以开火(士兵开火扣动的是扳机)
# 3）.枪 能够 发射子弹(把子弹发射出去)
# 4）.枪 能够 装填子弹 --增加子弹的数量

'''
'''




'''
class Gun(object):

    def __init__(self,name):
        self.name = name
        self.bullet_count = 0

    def __str__(self):
        return "制造一把%s有%d发子弹" % (self.name,self.bullet_count)

    def add_bullet(self):
        self.bullet_count += 20
        print('%d发子弹装填完毕'%self.bullet_count)

    def shot(self):
        self.bullet_count -= 1
        print('发射子弹1发，还剩%d发' % self.bullet_count)


class Soilder(object):

    def __init__(self,name):
        self.name = name
        # self.bullet = 0

    def __str__(self):
        return "士兵%s" % self.name

    def fire(self,item):

        if item.bullet_count > 0 :
            # print('%s子弹充足，进行射击' % item.name)
            print('士兵射击')
            item.shot()
        else:
            print('%s子弹不足，需要装填子弹' % item.name)
            item.add_bullet()



AK = Gun("AK47")
print(AK)

s1 = Soilder('瑞恩')
print(s1)
s1.fire(AK)
s1.fire(AK)
s1.fire(AK)
s1.fire(AK)

'''
'''
需求：
1）.房子有户型，总面积和家具名称列表
   新房子没有任何的家具
2）.家具有名字和占地面积，其中
   床：占4平米
   衣柜：占2平面
   餐桌：占1.5平米
3）.将以上三件家具添加到房子中
4）.打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表

'''
'''
需要定义的类：
房子类：House
属性：户型apartment   总面积total_area    家具名称列表furniture_list    剩余面积  residual_area 
方法：添加家具 add_furniture  


家具类：Furniture
属性：名字name  占地面积cover_area
方法：
'''
'''
class House(object):
    def __init__(self,apartment,total_area):
        self.apartment  = apartment
        self.furniture_list = []
        self.total_area = total_area
        self.residual_area = self.total_area
    def add_furniture(self,item):
        #面积减少&家具列表变多
        self.residual_area  = self.residual_area - item.area
        #self.furniture_list = \
        self.furniture_list.append(item.name)

        #pass
    def __str__(self):
        return '户型%s，总面积%d，剩余面积%d，家具名称列表%s'%(self.apartment,self.total_area,self.residual_area,self.furniture_list)
class Furniture(object):
    def __init__(self,name,cover_area):
        self.name = name
        self.area = cover_area
    def __str__(self):
        return '加了一个%s，面积是%d'%(self.name,self.area)


h = House('一室一厅',65)
print(h)
f = Furniture('床',45)
print(f)
h.add_furniture(f)
print(h)
'''
'''
class House(object):
    def  __init__(self,apartment,total_area):
        self.apartment = apartment
        self.total_area = total_area
        self.residual_area  =  self.total_area
        self.furniture_list = []
    def add_furniture(self,item):
        print('开始添加家具')
        if self.residual_area < item.cover_area:
            self.furniture_list = self.furniture_list
            self.residual_area = self.residual_area
            print('你的面积不够了')
        else:

            self.furniture_list.append(item.name)
            # if self.residual_area > item.cover_area:
            self.residual_area = self.residual_area - item.cover_area
            print('添加家具完成')
        # else:

        #print('添加家具完成')
        #家具名称列表新增
        #pass


        #面积减少（房子剩余面积，家具使用面积）
        #item.cover_area
    def __str__(self):
        return '创建了一个户型为%s,面积为%s平的房子,剩余面积为%d,家具有%s的房子'%(self.apartment,self.total_area,self.residual_area,self.furniture_list)
    #返回实例对象的类的描述信息，打印实例的时候，直接调用这个方法


class Furniture(object):
    def __init__(self,name,cover_area):
        self.name = name
        self.cover_area = cover_area
    def __str__(self):
        return '创建了一个%s家具,面积为%s的房子' % (self.name, self.cover_area)


#添加床，需要定义一个床
h = House('三室一厅',120)
# print(h)
f = Furniture('床',120)
#print(f)
h.add_furniture(f)
# print(f,f.name)#实例。属性名
print(h)
'''

'''
#士兵 Soldier
属性：name  
方法：开火  fire
#有  have

1）.士兵瑞恩有一把AK47
2）.士兵可以开火(士兵开火扣动的是扳机)
3）.枪 能够 发射子弹(把子弹发射出去)
4）.枪 能够 装填子弹 --增加子弹的数量

#枪 Gun
属性：name 
方法：装填 put  发射 Lunch
'''
class Soldier(object):
    def __init__(self,name):
        self.name = name
    def fire(self,item):
        if item.bullet > 0:


        #pass

    def __str__(self):
        return '士兵%s,有一把'%(self.name)
class Gun(object):
    def __init__(self,item,bullet):
        self.bullet = bullet
        self.item = item
    def put(self):
        if self.bullet > 0 :
            pass
        else:
            pass

    def lunch(self):
        pass
    def __str__(self):
        return '子弹还剩%s'%(self.bullet)

s = Soldier('ruien')
print(s)
g = Gun('ak47',100)
print(g)










'''







class Gun(object):

    def __init__(self,name):
        self.name = name
        self.bullet_count = 0

    def __str__(self):
        return "制造一把%s有%d发子弹" % (self.name,self.bullet_count)

    def add_bullet(self):
        self.bullet_count += 20
        print('%d发子弹装填完毕'%self.bullet_count)

    def shot(self):
        self.bullet_count -= 1
        print('发射子弹1发，还剩%d发' % self.bullet_count)


class Soilder(object):

    def __init__(self,name):
        self.name = name
        # self.bullet = 0

    def __str__(self):
        return "士兵%s" % self.name

    def fire(self,item):

        if item.bullet_count > 0 :
            # print('%s子弹充足，进行射击' % item.name)
            print('士兵射击')
            item.shot()
        else:
            print('%s子弹不足，需要装填子弹' % item.name)
            item.add_bullet()



AK = Gun("AK47")
print(AK)

s1 = Soilder('瑞恩')
print(s1)
s1.fire(AK)
s1.fire(AK)
s1.fire(AK)
s1.fire(AK)
'''