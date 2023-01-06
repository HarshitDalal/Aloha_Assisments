class A:
    def show(self):
        return f'Class A method'


class B(A):
    def showing(self):
        return f'class B Method'


class C(A):
    def detail(self):
        return f'Class C Method'


class Add:
    def add_n(self, a, b):
        return a + b


class Mul:
    def mul_n(self, a, b):
        return a * b


class Div:
    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError as e:
            return e


class Calculation(Add, Mul, Div):
    def avg(self, *args):
        return sum(args) / len(args)


if __name__ == '__main__':
    a = B()
    b = C()
    print(f'class B object call class A method {a.show()}')
    print(f'class B object call self method {a.showing()}')
    print(f'class C object call class A method {b.show()}')
    print(f'class C object call self method {b.detail()}')

    cal = Calculation()
    print(cal.avg(1, 2, 3, 4))

    print(cal.div(12, 2))
    print(cal.mul_n(2, 5))
    print(cal.add_n(2, 6))
