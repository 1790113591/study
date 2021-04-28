def jc1(n):
    r = 1
    while n > 1:
        r *= n
        n -= 1
    return r


def jc2(n):
    if n == 1:
        return 1
    return n * jc2(n-1)

if __name__ == '__main__':
    # 计算阶乘
    n = int(input("请输入一个数："))
    r = jc2(n)
    print("%d的阶乘为%d" % (n, r))