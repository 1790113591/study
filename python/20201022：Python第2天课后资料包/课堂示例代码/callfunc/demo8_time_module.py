import time

print("程序开始")
# time.sleep(5)  # 让程序休眠5秒（停下来5秒）


for n in range(10, 0, -1):
    time.sleep(1)
    print(n)

print("\n程序结束")