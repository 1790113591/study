a = int(input("请输入第一条边的长度："))
b = int(input("请输入第二条边的长度："))
c = int(input("请输入第三条边的长度："))

# 分析：任意的两边之和大于第三边（默认是正数）
if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("等边三角形")
    elif a == b or b == c or a == c:
        print("等腰三角形")
    else:
        print("普通三角形")
else:
    print("无法构成三角形")

print("\n程序结束！")
