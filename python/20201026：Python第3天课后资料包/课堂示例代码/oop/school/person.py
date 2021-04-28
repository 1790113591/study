class Person:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def sayhi(self):
        print("大家好，我是%s，今年%s岁。" % (self.name, self.age))
