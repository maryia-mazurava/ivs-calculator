"""!
    @file basic.py

    @brief Implementation of the basic mathematical operations library for the calculator.

    @author Alina Vinogradova

    @date 26.04.2023

"""


class Basic:
    """!
        @brief Base class "Basic", representation of basic mathematical operations
    """

    pi = 3.1416
    exp = 2.7183

    def __init__(self):
        pass

    def add(self, x: float, y: float):
        """!
            @brief Method for + operation
            @param x First operand
            @param y Second operand
            @return Sum of two numbers
        """

        return self.int_translate(x + y)

    def sub(self, minuend: float, subtrahend: float):
        """!
            @brief Method for - operation
            @param minuend First operand
            @param subtrahend Second operand
            @return Difference between two numbers
        """

        return self.int_translate(minuend - subtrahend)

    def mul(self, multiplier: float, multiplicant: float):
        """!
            @brief Method for * operation
            @param multiplier First operand
            @param multiplicant Second operand
            @return Product of two numbers
        """

        return self.int_translate(multiplier * multiplicant)

    def div(self, divident: float, divisor: float):
        """!
            @brief Method for / operation
            @param divident The number to be divided
            @param divisor The number to divide by
            @return Division operation result
        """

        if divisor == 0:
            raise ZeroDivisionError
        else:
            return self.int_translate(divident / divisor)


    @staticmethod
    def int_translate(num):
        """!
            @brief Method for making an integer number of float
            @param num The number to be rounded
            @return Rounded number
        """

        if isinstance(num, complex):
            num = num.real
        if float(num).is_integer():
            return int(num)
        else:
            return round(num, 7)

