from deffunc.demo10_function_define import get_sum2, get_sum3, get_sum4

# 传入实际的参数要符合定义函数时，定义的参数格式
print("1到100的和：", get_sum2())
print()
print("50到100的和：", get_sum2(50))  # 计算的是50到100的和
print()
print("1到50的和：", get_sum2(b=50))  # 计算的是1到50的和
print()
print("50到70的和：", get_sum2(a=50, b=70))
print()
print("50到70的和：", get_sum2(50, 70))
print()

print("50到70的和：", get_sum2(b=70, a=50))
print()

print("50到100的和：", get_sum3(50, 100))
print("50到100的和：", get_sum3(50))

print()
print("第1组总分：", get_sum4(78, 96, 54, 79, 91))
print("第2组总分：", get_sum4(76, 63, 92))
print("第3组总分：", get_sum4(76))
print("第4组总分：", get_sum4())
# 调用的时候，可以使用【*容器数据】，将容器中的元素拆包，一个一个的传入函数
print("第5组总分：", get_sum4(*[88, 96, 54, 79]))

