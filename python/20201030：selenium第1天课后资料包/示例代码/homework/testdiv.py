import unittest

from homework.calc import Calc
from homework.mytest import BaseTest


class TestDiv(BaseTest):

    # 测试用例01
    def test_div1(self):
        c = Calc()  # 创建了一个计算器类（Calc）的对象
        self.assertEqual(-0.6, c.div(3, -5))

    # 测试用例02
    def test_div2(self):
        c = Calc()  # 创建了一个计算器类（Calc）的对象
        actual = c.div(0, 3)
        self.assertEqual(0, actual)


if __name__ == '__main__':
    unittest.main()