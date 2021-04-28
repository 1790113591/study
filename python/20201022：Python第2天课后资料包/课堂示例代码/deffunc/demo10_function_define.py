from random import random


# 定义函数
def say_love():
    print("我爱你，亲爱的")
    print("我要永远和你在一起")


# 定义函数
def eat():
    print("正在吃东西")
    return random() > 0.5


# 定义了一个函数
def get_sum():
    s = 0
    n = 1
    while n <= 100:
        s += n
        n += 1
    return s


# 定义了一个函数，定义了2个形参（形式参数）
# start的默认值为1，不传参的时候，当做1来使用
# end的默认值为100，不传参的时候，当做100来使用
def get_sum2(a=1, b=100):
    s = 0
    n = a
    while n <= b:
        s += n
        n += 1
    return s

# 当形参中既有无默认值的，又有有默认值的参数时，无默认值的要定义在前面
def get_sum3(a, b=100):
    s = 0
    n = a
    while n <= b:
        s += n
        n += 1
    return s

# 定义函数时，不确认未来调用者会传入多少个参数
# 可变参数：【*形参名】来代表传入的所有的参数，将其收集起来形成一个元组
def get_sum4(*scores):
    print("\n【scores】", scores)
    s = 0
    for sc in scores:
        s += sc
    return s

# 定义一个变量
version = "3.0.12.107"
