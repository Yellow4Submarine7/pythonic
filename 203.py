lax_coordinates = (33.9425,-118.408056)
city,year,pop,chg,area = ('Tokyo',2003,32450,0.66,8014)#这也是拆包
traveler_ids = [('USA','31195855'),('BRA','CE342567'),('ESP','XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s'%passport)
#for后跟两个变量，对应元组中的两个量，这被称为拆包
#元素拆包可应用到任何可迭代对象上
for country,_ in traveler_ids:
    print(country)
a,b = 0,1
b,a = a,b #这也是拆包的一种
#还可用*运算符把一个可迭代的对象拆开作为函数的参数
#类似于指针
divmod(20,8)
t = (20,8)
divmod(*t)


