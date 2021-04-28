from unittest import TestSuite, TextTestRunner
from homework.testdiv import TestDiv
from homework.testmul import TestMul

# 使用TestSuite类构建测试套件并执行测试

suite = TestSuite()
suite.addTest(TestDiv("test_div1"))
suite.addTest(TestDiv("test_div2"))
suite.addTests([TestMul("test_mul1"), TestMul("test_mul2")])

runner = TextTestRunner(verbosity=2)
runner.run(suite)
