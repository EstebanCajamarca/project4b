# Author: Esteban Cajamarca
# GitHub username: EstebanCajamarca
# Date: 1/24/2022

# The first and second numbers in the Fibonacci sequence are both 1. After that, each subsequent number is the sum of
# the two preceding numbers. The first several numbers in the sequence are: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
# etc. Write a function named fib that takes a positive integer parameter and returns the number at that position of
# the Fibonacci sequence. For example fib(1) = 1, fib(3) = 2, fib(10) = 55, etc. Your function does not need to print
# anything out - just return a value.


def fib(n):
    a = 0
    b = 1
    # Condition if integer entered is less than zero.
    if n < 0:
        print("Incorrect input, please enter positive integer")
    # if n is equal to zero then fib takes the value of variable a.
    elif n == 0:
        """Returns 0."""
        return a
    # if n is equal to one, then fib takes value of variable b.
    elif n == 1:
        """Returns 1."""
        return b
    # for all integers different from one and zero, fib obeys the following:
    else:
        # range foes fromm 2 to entered value fib plus one.
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b


# test
# print(fib(1))
# print(fib(3))
# print(fib(10))
