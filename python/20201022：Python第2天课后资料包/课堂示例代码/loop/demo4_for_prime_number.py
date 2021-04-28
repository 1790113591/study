"""
    判断用户输入的整数是否是素数
"""
number = int(input("请输入一个数字："))
if number < 2:
    print("%d不是素数" % number)
else:
    for i in range(2, number):
        if number % i == 0:
            print("%d不是素数，可以被%d除尽" % (number, i))
            break
        i = 100
    else:
        print("%d是素数" % number)