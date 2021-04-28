class Student:

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("一个人在吃" + food)

    def exam(self, course):
        print("正在考试：" + course)


if __name__ == '__main__':
    s = Student("张三")
    print(s)
