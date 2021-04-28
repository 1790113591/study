# 传入2个参数时候：前闭后开
for n in range(5, 21):
    print(n, end=" ")
print()

# 传入1个参数的时候：产生0到这个参数-1的一组数字
for n in range(10):
    print(n, end=" ")
print()


# 传入3个参数的时候：第3个参数是“步长（step）”
for n in range(10, 40, 1):
    print(n, end=" ")
print()
for n in range(10, 40, 3):
    print(n, end=" ")
print()
# 第3个参数为负数，第1个参数必须大于第2个参数：从大到小了
for n in range(40, 10, -1):
    print(n, end=" ")
print()
for n in range(40, 10, -5):
    print(n, end=" ")
print()