from oop.school.person import Person


class Teacher(Person):

    def __init__(self, name, age, sex, year):
        super().__init__(name, age, sex)
        self.year = year

    def teaching(self):
        print("%s老师正在上课，他已经有%s年的教学经验了" % (self.name, self.year))


if __name__ == '__main__':
    wdz = Teacher("王德柱", 39, "男", 15)
    wdz.sayhi()  # 继承自父类Person类的sayhi方法
    wdz.teaching()
