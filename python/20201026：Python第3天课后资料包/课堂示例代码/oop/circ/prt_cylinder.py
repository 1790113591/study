# 组员A：
from oop.circ.def_circle import Cylinder

print("====================== 圆柱计算小程序 =====================\n")
r = float(input("请输入圆柱底面的半径："))
h = float(input("请输入圆柱的高："))

# 创建了一个圆柱类的实例对象cylinder
cylinder = Cylinder(r, h)
p = cylinder.calc_circle()  # 调用圆柱对象cylinder的计算底面周长的方法
s = cylinder.calc_area()  # 调用圆柱对象cylinder的计算底面面积的方法
v = cylinder.calc_volume()  # 调用圆柱对象cylinder的计算体积的方法

print("\n底面半径为%s的圆柱的底面周长为%.3f" % (r, p))
print("底面半径为%s的圆柱的底面面积为%.3f" % (r, s))
print("底面半径为%s，高为%s的圆柱的体积为%.3f" % (r, h, v))
