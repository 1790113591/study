import unittest

from homework.calc import Calc
from homework.mytest import BaseTest


class TestMul(BaseTest):

    # 测试用例01
    def test_mul1(self):
        c = Calc()  # 创建了一个计算器类（Calc）的对象
        self.assertEqual(-15, c.mul(3, -5))

    # 测试用例02
    def test_mul2(self):
        c = Calc()  # 创建了一个计算器类（Calc）的对象
        actual = c.mul(3, 0)
        self.assertEqual(0, actual)


if __name__ == '__main__':
    unittest.main()