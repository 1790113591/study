"""
    编程实现输入某年某月某日，输出它是这一年的第几天
"""
from datetime import date  # 从日期时间模块中，导入date函数

print("========================== 天数计算小程序 =========================\n")
year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))

#
# 使用了datetime模块中的date函数
#
# 方式（一）
# # date函数，可以根据传入的年、月、日，构造一个date类的标准日期
# target = date(year, month, day)  # 将指定的年月日构造成一个标准日期
# last = date(year - 1, 12, 31)  # 将指定的年份的上一年的最后一天，构造成一个标准日期
# # date类的标准日期之间，可以用加号，求天数差
# print(target - last)
# 方式（二）
# target = date(year, month, day)  # 将指定的年月日构造成一个标准日期
# days = target.strftime("%j")  # 获取日期是这一年中的第多少天
# print("%d年%d月%d日是这一年中的第%s天" % (year, month, day, days))

#
# 自己写算法
# 将指定月份前的每月天数累加，然后再加上指定的日期的日期数
# 例如：2020年8月4日，那么用2020年1月至7月的总天数 + 4
#
# （一）
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     days_of_feb = 29
# else:
#     days_of_feb = 28
# #           1月    2月       3月 4月 5月 6月 7月 8月 9月 10月 11月
# days_list = [31, days_of_feb, 31, 30, 31, 30, 31, 31, 30, 31, 30]
# #            0      1         2   3   4   5   6   7   8   9   10
# total_days = 0
# for i in range(1, month):
#     total_days += days_list[i - 1]
# total_days += day
# print("%d年%d月%d日是这一年中的第%s天" % (year, month, day, total_days))


# （二）
# 从1月开始，累加每个月的天数，直到month-1月
total_days = 0
for m in range(1, month):
    if m in (1, 3, 5, 7, 8, 10, 12):
        total_days += 31
    elif m in (4, 6, 9, 11):
        total_days += 30
    elif m == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            total_days += 29
        else:
            total_days += 28

total_days += day
print("%d年%d月%d日是这一年中的第%s天" % (year, month, day, total_days))