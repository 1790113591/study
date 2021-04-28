from unittest import TestLoader, TextTestRunner

# 使用TestLoader类的discover()来自动发现测试用例并执行

all_tests = TestLoader().discover("homework")

r = TextTestRunner(verbosity=2)
r.run(all_tests)

