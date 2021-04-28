# 组员B：圆形类的定义者，定义类给组员A
# 定义的圆形类，必须要支持有一个属性为半径
# 还要有计算圆形面积和周长的方法


class Circle:
    # 类属性，整个类共享的，不管创建多少个对象，内存中只有一个类属性
    # 在类的内部，既可以用self来访问，也可以用类名来访问，但推荐用类名来访问
    # 在类的外部，可以直接使用类名来访问，也可以用对象名类访问
    PI = 3.14  # 圆周率

    # 定义一个构造方法，接收一个代表圆的半径的参数
    def __init__(self, r):
        # 定义了圆的“半径”属性：self.radius
        # 实例属性，每一个对象，都有自己的实例属性，占一份内存空间
        # 实例属性，只能用self来访问
        self.radius = r

    # 定义一个计算周长的方法，计算并返回自己周长
    def calc_circle(self):
        zc = 2 * Circle.PI * self.radius
        return zc

    # 定义一个计算面积的方法，计算并返回自己的面积
    def calc_area(self):
        mj = Circle.PI * self.radius ** 2
        return mj


# 定义圆柱类
class Cylinder(Circle):

    def __init__(self, r, h):
        super().__init__(r)
        self.height = h

    # 定义一个圆柱体积的方法
    def calc_volume(self):
        # self.calc_area() 调用了自己类中或父类中的的其他方法
        tj = self.calc_area() * self.height
        return tj


# 定义圆锥类
class Cone(Cylinder):

    # 定义一个圆锥体积的计算方法
    def calc_volume(self):
        tj = super().calc_volume() / 3
        return tj