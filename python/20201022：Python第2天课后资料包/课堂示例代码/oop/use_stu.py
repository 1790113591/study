from oop import stu

#
# 创建几个学生对象，让学生做一些事：考试、打招呼
#

# 创建了一个Student类的对象，用zs来代表这个对象，zs也被叫做对象名（变量名）
zs = stu.Student("张三", 25, "男")
print(zs.name)  # 访问zs对象的name属性
print(zs.age)

zs.exam("语文")  # 调用了Student类的zs对象的exam方法
zs.exam("数学")  # 调用了Student类的zs对象的exam方法
zs.sayhi()  # 调用了Student类的zs对象的exam方法


print()

# 创建对象的本质，就是调用这个类的构造方法__init__
ls = stu.Student("李四", 24, "女")
ls.sayhi()
ls.exam("英语")

