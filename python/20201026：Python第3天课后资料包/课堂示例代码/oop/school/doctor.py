from oop.school.person import Person
from oop.school.student import Student
from oop.school.teacher import Teacher


class Doctor(Person):

    def checking(self, p):
        print("医生%s正在给病人%s进行检查" % (self.name, p.name))


if __name__ == '__main__':
    zzr = Student("周芷若", 25, "女", "S1013", "全程5期")
    wdz = Teacher("王德柱", 39, "男", 15)

    lzj = Doctor("刘正江", 37, "男")
    lzj.sayhi()
    lzj.checking(zzr)
    lzj.checking(wdz)

