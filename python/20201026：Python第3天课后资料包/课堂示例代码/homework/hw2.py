"""
编写一个student类，包含姓名、性别、年龄、家庭住址，并在info()方法中显示这些信息。
根据类生成两个对象s1、s2，并分别调用对象的info()方法输出学员的信息。
"""


class Student:

    # 构造方法的方法名必须固定为：__init__
    # 这个方法是在未来，创建类的对象（实例）时，由系统自动调用
    def __init__(self, name, age, sex='男', address='成都市'):
        # self.属性名 ，是在为类定义属性
        self.name = name
        self.sex = sex
        self.age = age
        self.address = address

    def info(self):
        print("\n学生信息详情如下：")
        print("姓名：", self.name)  # 访问name属性
        print("性别：", self.sex)
        print("年龄：", self.age)
        print("住址：", self.address)


if __name__ == '__main__':
    zs = Student("张三", 23)  # 创建对象(object)/实例(instance)
    ls = Student("李四", 24, "女")
    ww = Student("王五", 25, address="内蒙古")

    zs.info()  # 打印出学生对象的信息
    ww.info()  # 调用方法，必须要在方法名后面打小括
    ww.info()
    ls.info()
