#import os
#lax_coordinates = (33.9425,-118.408056)
#city,year,pop,chg,area = ('Tokyo',2003,32450,0.66,8014)#这也是拆包
#traveler_ids = [('USA','31195855'),('BRA','CE342567'),('ESP','XDA205856')]
#for passport in sorted(traveler_ids):
#    print('%s/%s'%passport)
##for后跟两个变量，对应元组中的两个量，这被称为拆包
##元素拆包可应用到任何可迭代对象上
#for country,_ in traveler_ids:
#    print(country)
#a,b = 0,1
#b,a = a,b #这也是拆包的一种
##还可用*运算符把一个可迭代的对象拆开作为函数的参数
##类似于指针
#divmod(20,8)
#t = (20,8)
#print(divmod(*t))
#print(divmod(t))#这样不行，divmod需要两个参数
#
#
##用_占位符处理不需要的元组元素
#_,filename = os.path.split('~/test.py')
#print(filename)

#用*前缀处理不需要的不定量参数
#a,b,*rest = range(5)
#print(rest)     # [2,3,4]

#创建具名元组,这个具名元组其实是一个类
from collections import namedtuple
City = namedtuple('City','name country population coordinates')
tokyo = City('Tokyo' ,'JP' ,36.933,(35.4598,139.3344))
#print(tokyo.population)
#print(tokyo)
#具名元组拥有_fields类属性，_make(iterable)类方法,_asdict()实例方法
print(City._fields)
LatLong = namedtuple('LatLong','lat long')#经纬度的具名元组
delhi_data = ('Delhi NCR','IN',21.935, LatLong(28.613889,77.208889))
delhi = City._make(delhi_data)#make 接受一个可迭代的对象来生成类的实例
delhi = City(*delhi_data) #作用与上面相同
print(delhi._asdict())#使用asdict将元组里的信息友好的呈现出来







