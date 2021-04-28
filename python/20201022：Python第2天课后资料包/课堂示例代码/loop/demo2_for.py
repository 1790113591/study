for b in ("西游记", "红楼梦", "水浒传", "三国演义"):
    print("《" + b + "》", end="  ")

print()
for b in [89, 93, 78, 96, 52, 91]:
    print(str(b) + "分", end="  ")

print()
for stu in {"S1013": "张无忌", "S1019": "赵敏", "S2001": "周芷若"}:
    print(stu, end="  ")

print()
scores = [89, 93, 78, 96, 52, 91]
for s in scores:
    print(s, end=" ")
print("\n")

# 计算1到20连续自然数的和
s = 0
n = 1
while n <= 20:
    s += n
    n += 1
print("和：", s)

s = 0
for n in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20):
    s += n
print("和：", s)

# 使用for和range函数来搭配
# range函数负责生成一组有规律数字的容器
# range函数传入2个参数的时候，前闭后开
s = 0
for n in range(1, 21):
    s += n
print("和：", s)
