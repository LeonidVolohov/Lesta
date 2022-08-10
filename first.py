import unittest
import timeit


"""
Первый алгоритм находит четность числа по остатку от деления на 2, второй же по оператору логического сложения.
Идея заключается в том, что если имеется последний бит у числа, то это число нечетное, в противном случае - четное.

Сложно выделить какие-о плюсы и минусы, однако если говорить о "простоте" и "читаемости" кода, то первый алгоритм
(is_even) более прост в понимании. Однако в защиту второго можно сказать, что он выполняется чуть быстрее,
относительно первого

is_even - 0.39661706396145746
is_even_another - 0.2568016249570064
"""
def is_even(number: int) -> bool:
    return True if number % 2 == 0 else False

def is_even_another(number: int) -> bool:
    return False if number & 1 else True


class TestIsEven(unittest.TestCase):
    def test_even(self):
        self.assertEqual(is_even(2), True)
        self.assertEqual(is_even(4), True)
        self.assertEqual(is_even(6), True)
        self.assertEqual(is_even(8), True)

        self.assertEqual(is_even_another(2), True)
        self.assertEqual(is_even_another(4), True)
        self.assertEqual(is_even_another(6), True)
        self.assertEqual(is_even_another(8), True)

    def test_odd(self):
        self.assertEqual(is_even(1), False)
        self.assertEqual(is_even(3), False)
        self.assertEqual(is_even(7), False)
        self.assertEqual(is_even(9), False)

        self.assertEqual(is_even_another(1), False)
        self.assertEqual(is_even_another(3), False)
        self.assertEqual(is_even_another(7), False)
        self.assertEqual(is_even_another(9), False)


def main():
    # unittest.main()

    print("is_even - " + \
        str(timeit.timeit("is_even(1000000000000000000000000)", setup="from __main__ import is_even")))
    print("is_even_another - " + \
        str(timeit.timeit("is_even_another(1000000000000000000000000)", setup="from __main__ import is_even_another")))

if __name__ == "__main__":
    main()
