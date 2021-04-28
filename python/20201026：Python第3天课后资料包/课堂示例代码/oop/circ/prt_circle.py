from oop.circ.def_circle import Circle

# 组员A：
print("====================== 圆形计算小程序 =====================\n")
r = float(input("请输入圆的半径："))

# 有一个Circle类，代表圆形的类，它有一个属性叫做radius，代表半径
# 它还有2个方法，一个是calc_circle，用来计算自己的周长
# 还有一个是calc_area，用例计算自己的面积

c = Circle(r)  # 创建一个Circle类的实例对象，并传入的r作为参数来给圆对象的半径属性赋值
p = c.calc_circle()  # 调用Circle类的对象c的计算周长的方法calc_circle，得到一个返回值
s = c.calc_area()  # 调用Circle类的对象c的计算面积的方法calc_circle，得到一个返回值

print("\n半径为%s的圆的周长为%.3f" % (r, p))
print("半径为%s的圆的面积为%.3f" % (r, s))
