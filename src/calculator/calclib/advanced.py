"""!
    @file advanced.py

    @brief Implementation of advanced mathematical operations library for the calculator.

    @author Alina Vinogradova

    @date 26.04.2023

"""


import sys

from . import basic
from . import exceptions as e
import math


class Advanced(basic.Basic):
    """!
    @brief Base class "Advanced", representation of advanced mathematical operations
    """

    def __init__(self):
        self.basic = basic.Basic()

    def power(self, base: float, exponent: float) -> float:
        """!
            @brief Method for exponentiation operation
            @param base Base number
            @param exponent Exponent number
            @return Power of the given number
        """

        return self.int_translate(pow(base, exponent))

    def factorial(self, x: int) -> int:
        """!
            @brief Method for factorial computation
            @param x Operand
            @return Factorial of a given number
        """

        try:
            if x < 0 or isinstance(x, float):
                raise e.BadOperandException

            result = 1
            for num in range(1, x + 1):
                result = result * num
            return self.int_translate(result)
        except e.BadOperandException:
            sys.stderr.write("Error: wrong factorial operand")

    def logarithm(self, number: float, base: int) -> float:
        """!
            @brief Method for logarithms computation
            @param base Base number
            @param number Antilogarithm number
            @return Logarithm value of given number with specific base
        """

        try:
            if base == 1 or base <= 0 or number <= 0:
                raise e.BadOperandException
        except e.BadOperandException:
            sys.stderr.write("Error: wrong logarithm base")

        return self.int_translate(math.log(number, base))

    def rootn(self, degree: int, radicand: float):
        """!
            @brief Method for n-th root computations
            @param self Object pointer
            @param degree Root degree
            @param radicand The number from which the root has to be extracted
        """

        try:
            if degree % 2 == 0 and radicand < 0:
                raise e.BadOperandException
        except e.BadOperandException:
            sys.stderr.write("Error: wrong root expression")

        return self.int_translate(self.power(radicand, self.power(degree, -1)))

    def sinus(self, x):
        """!
            @brief Method for sinus function
            @param x An angle in radians (pi/2, pi/4, pi/3, etc.)
            @return The sine of the given parameter value
        """

        return self.int_translate(math.sin(x))

    def cosines(self, x):
        """!
            @brief Method for cosines function
            @param x An angle in radians (pi/2, pi/4, pi/3, etc.)
            @return The cosine of the given parameter value
        """

        return self.int_translate(math.cos(x))

    def tang(self, x):
        """!
            @brief Method for tangents function
            @param x An angle in radians (pi/2, pi/4, pi/3, etc.)
            @return The tangent  of the given parameter value
        """

        return self.div(self.sinus(x), self.cosines(x))

    def cotg(self, x):
        """!
            @brief Method for cotangents function
            @param x An angle in radians (pi/2, pi/4, pi/3, etc.)
            @return The cotangent  of the given parameter value
        """
        return self.div(self.cosines(x), self.sinus(x))
