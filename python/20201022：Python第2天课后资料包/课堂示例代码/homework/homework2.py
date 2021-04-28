number = int(input("请输入一个整数："))
if number < 2:
    print("%d不是素数" % number)
else:  # number是大于或等于2的范围了
    i = 2  # 从2开始的不断去除number的整数
    while i < number:
        if number % i == 0:
            print("%d不是素数，能被%d除尽" % (number, i))
            break
        i += 1
    else:
        print("%d是素数" % number)

print("\n程序结束！")