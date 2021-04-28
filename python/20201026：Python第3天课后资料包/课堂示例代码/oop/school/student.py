from random import randint
from oop.school import person


class Student(person.Person):

    # 重写了父类的__init__方法
    # 父类中已经定了构造方法，子类重新定义一遍
    def __init__(self, name, age, sex, sno, klass):
        # 调用父类的构造方法，传入对应的形参
        super().__init__(name, age, sex)
        self.sno = sno
        self.klass = klass

    def exam(self, course):
        print("学号%s的%s，进行了%s科目的考试" % (self.sno, self.name, course))
        return randint(0, 100)


if __name__ == '__main__':
    zzr = Student("周芷若", 25, "女", "S1013", "全程5期")
    print(zzr.name)
    print(zzr.age)
    print(zzr.sex)
    zzr.sayhi()  # 父类的普通方法继承下来了
    zzr.exam("MySQL数据库")