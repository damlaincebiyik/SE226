import math


def factorial(x: int) -> int:
    # Using the recursive factorial function from question 1
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)


def sine_x(x: float, n: int) -> float:
    x_rad = x * math.pi / 180

    # Lambda function, though it should be def
    term = lambda i: ((-1) ** i) * (x_rad ** (2 * i + 1)) / factorial(2 * i + 1)

    result = 0
    for j in range(n + 1):
        result += term(j)

    return result


class HarmonicNumber:

    def __init__(self):
        self._harmonic_sum = 0

    def harmonic_number(self, n: float) -> None:
        """
        Calculate the nth harmonic number recursively using a global variable.

        The harmonic number Hn is defined as:
        Hn = 1 + 1/2 + 1/3 + ... + 1/n

        The function uses recursion to calculate the sum and updates the global
        variable 'harmonic_sum' instead of returning a value.

        """

        if n <= 0:
            return

        if n == 1:
            self._harmonic_sum = 1
            return

        self.harmonic_number(n - 1)

        self._harmonic_sum += 1 / n

    def get_harmonic_sum(self) -> float:
        return self._harmonic_sum