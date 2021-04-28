# 组员A：
from oop.circ.def_circle import Cone

print("====================== 圆锥计算小程序 =====================\n")
r = float(input("请输入圆锥底面的半径："))
h = float(input("请输入圆锥的高："))

cone = Cone(r, h)
p = cone.calc_circle()
s = cone.calc_area()
v = cone.calc_volume()
print("\n底面半径为%s的圆锥的底面周长为%.3f" % (r, p))
print("底面半径为%s的圆锥的底面面积为%.3f" % (r, s))
print("底面半径为%s，高为%s的圆锥的体积为%.3f" % (r, h, v))
