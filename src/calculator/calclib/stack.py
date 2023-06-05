"""!
    @file stack.py

    @brief Implementation of the stack for expression parsing

    @author Alina Vinogradova

    @date 26.04.2023

"""

import sys


class Stack:
    """!
        @brief Base class Stack, representation of standard manipulations with stack
    """

    def __init__(self):
        self.items = []

    def push(self, obj):
        """! @brief Push given object on top of the stack """
        self.items.append(obj)

    def pop(self):
        """! @brief Pop an object from the stack"""

        if self.is_empty():
            raise IndexError("Empty stack.")
        return self.items.pop()

    def size(self) -> int:
        """! @brief Returns size of a stack"""

        return len(self.items)

    def top(self):
        """! @brief Returns object on top of the stack"""

        return self.items[-1]

    def is_empty(self) -> bool:
        """! @brief Checking if the stack is empty """

        return self.size() == 0

    def print(self):
        """! @brief Prints the full stack to stderr"""

        sys.stderr.write("\t--- Stack bottom")
        for i in self.items:
            i.print()
        sys.stderr.write("\tStack top ---")

    def clear(self):
        """! @brief Clears the stack """

        self.items = []
