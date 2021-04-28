# 组员A:
from deffunc.prime.util import isprime

print("=============== 打印500到800之间的素数 ==================\n")

for n in range(500, 801):
    if isprime(n):
        print(n, end=" ")

print("\n谢谢使用！")
