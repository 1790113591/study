# 组员B：
def isprime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# 入口点：仅当python解释器执行运行当前这个文件时，才执行的代码
if __name__ == '__main__':
    # 调用一下，用几组数据
    print("isprime(-1):", isprime(-1))
    print("isprime(0):", isprime(0))
    print("isprime(1):", isprime(1))
    print("isprime(2):", isprime(2))
    print("isprime(9):", isprime(9))
    print("isprime(121):", isprime(121))
    print("isprime(3907):", isprime(3907))
