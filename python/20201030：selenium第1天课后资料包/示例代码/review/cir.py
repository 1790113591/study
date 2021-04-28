class Circle:

    def calc_area(self, r):
        return 3.14 * r ** 2

    def calc_circle(self, r):
        return 3.14 * 2 * r


class Circle2:

    def __init__(self, r):
        self.r = r

    def calc_area(self):
        return 3.14 * self.r ** 2

    def calc_circle(self):
        return 3.14 * 2 * self.r


if __name__ == '__main__':
    c2 = Circle2(5)
    print(c2.calc_area())
    print(c2.calc_circle())
    print()
    c =  Circle()
    print(c.calc_circle(5))
    print(c.calc_area(5))