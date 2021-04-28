from random import randint

from deffunc.demo10_function_define import say_love, eat, get_sum

print(say_love())  # 调用函数

print(eat())  # 调用函数，并将返回值直接打印

f = eat()  # 调用函数，并将返回值保存至变量f中
print(f)

print()
while eat():
    print("没吃饱")


print("\n调用了get_sum函数：")
print("1到100的和是：", get_sum())
print("连续的1到100的和是：", get_sum())

print("\n===========================================\n")
r = 37.62
s = 3.14 * r ** 2
s = round(s, 2)  # 调用round的时候，你希不希望它打印出：4443.9328531四舍五入的结果是4443.93
print("圆的面积是：", s)

