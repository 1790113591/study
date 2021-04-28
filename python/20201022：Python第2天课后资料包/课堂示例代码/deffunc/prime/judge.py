from deffunc.prime.util import isprime

# 组员A:
print("================ 素数判断 ==================\n")
number = int(input("请输入一个数字："))

# 找素数判断的函数来帮忙：调用函数
if isprime(number):
    print("%d是素数！" % number)
else:
    print("%d不是素数！" % number)

print("\n程序结束！")
