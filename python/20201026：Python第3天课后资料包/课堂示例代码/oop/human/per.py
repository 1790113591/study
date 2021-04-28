class Person(object):

    def __init__(self, name):
        self.name = name

    def smile(self):
        print("一个人%s在笑" % self.name)


class Man(Person):

    def smile(self):
        print("一个人%s在嘿嘿地笑" % self.name)


class Woman(Person):

    def smile(self):
        print("一个人%s在嘻嘻地笑" % self.name)


# 定义一个进行微笑比赛的函数，需要接受一个参加比赛的人
# 参数是Person类的对象就可以，可以smile就行
def pksmile(per):
    if isinstance(per, Person):
        print("\n%s参加了微笑大赛" % per.name)
        per.smile()  # 调用人的微笑的方法
    else:
        print("\n无效的数据类型【%s】，必须传入一个Person类的对象实例" % type(per))
