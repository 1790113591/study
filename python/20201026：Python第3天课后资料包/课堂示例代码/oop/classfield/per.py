class Person:

    history = 200  # 人类的历史
    amount = 74  # 人口数量

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayhi(self):
        print("大家好，我是%s，今年%s" % (self.name, self.age))
        print("我来介绍人类的发展，人口已经有%s万年的历史了" % Person.history)
        print("目前，地球上已经有%s亿人口" % Person.amount)


if __name__ == '__main__':
    print("人类历史：", Person.history)
    # print(Person.name)  # 报错