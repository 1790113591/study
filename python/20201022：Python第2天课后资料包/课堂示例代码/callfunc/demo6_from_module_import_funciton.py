from random import randint  # 从random模块中导入randint函数
from random import random  # 从random模块中导入random函数

from random import randint, random, choice  # 从1个模块中，导入多个函数


# randint函数：产生指定范围的随机整数：前闭后闭
r = randint(1, 100)
print("随机的1到100之间的整数：", r)

# random函数：产生0到1之间的随机小数：不超过1
print(random())

# choice函数：能从容其中，随机选择返回一个元素
print(choice(["西游记", "三国演义", "水浒传", "红楼梦"]))