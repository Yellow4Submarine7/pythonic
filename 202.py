#symbols = '@#$%^&*'
##使用列表推导替代平常的for循环
##codes = [ord(symbol
##    ) for symbol in
##    symbols
##    ]
#
##print(codes)
##一般原则是如果列表推导代码超过两行那么应该考虑用for循环重写
##python 会忽略代码里[],{}和()中的换行，因此可以省略续行符\
#
##使用map/filter组合替代列表推导
#beyond_ascii_1 = [ord(s) for s in symbols if ord(s) > 127]
##filter(判断函数，遍历对象),lambda提供一个匿名函数
#beyond_ascii_2 = list(filter(lambda c: c > 127, map(ord,symbols)))

#使用列表推导计算笛卡尔积
colors = ['black','white']
sizes = ['S','M','L']
tshirts = [(color,size) for color in colors for size in sizes]
print(tshirts)

#如果想生成列表以外其他类型的序列，应该使用生成器表达式
#生成器是逐个地产出元素，而不是先建立一个完整的列表
#生成器与列表推导的主要区别是圆括号换成了方括号
symbols = '@#$%^&'
print(tuple(ord(symbol) for symbol in symbols))








