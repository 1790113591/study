# 定义了一个Student类，代表一个学生
class Student:

    # 它是类的初始化方法（固定的特殊方法），一定有
    # 不是让对象来调用的，是当我们用类名来创建对象时，系统自动调用的
    def __init__(self, name, age, sex):
        self.name = name  # 定义姓名属性
        self.age = age  # 定义年龄属性
        self.sex = sex  # 定义性别属性

    # 学生参加考试的方法
    def exam(self, course):
        self.sayhi()  # 使用self调用本类中的其他方法
        print("学生%s正在进行%s科目的考试" % (self.name, course))

    # 学生打招呼的方法
    def sayhi(self):
        print("大家好，我叫%s，今年%d岁，我是一个%s生。" % (self.name, self.age, self.sex))


