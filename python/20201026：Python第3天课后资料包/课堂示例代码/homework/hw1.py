"""
    编写函数sum(n)，该函数可以用来计算1~n的和。
"""

def sum(n):
    s = 0  # 总和
    for i in range(1, n + 1):
        s += i
    return s


if __name__ == '__main__':
    print("测试一下sum函数")
    print("sum(10)的返回值为:", sum(10))
    print("sum(100)的返回值为:", sum(100))
