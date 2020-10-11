#!/usr/bin/env python3

"""fib.py: fibonacci sequence functions"""
__author__ = "Jessica Lynch"

# Global error messages
errors = ["Sequence index must be 1 or greater",
          "Exponent must be positive",
          "Integer must be positive"
          "Value must be integer"
          ]


def fib_recur(x):
    """Returns the xth value of the fibonacci sequence via recursion"""
    if x < 1:
        raise ValueError(errors[0])
    elif x == 1 or x == 2:
        return x - 1
    else:
        return fib_recur(x - 1) + fib_recur(x - 2)


def fib_cache(x):
    """Returns the xth value of the fibonacci sequence via recursion
    and a cache table to avoid repeat calculations"""
    if x < 1:
        raise ValueError(errors[0])
    else:
        cache = {}
        return fib_cache_helper(x - 1, cache)


def fib_cache_helper(x, cache):
    """Helper function for fib_cache"""
    if x == 0 or x == 1:
        return x
    elif x in cache:
        return cache[x]
    else:
        cache[x] = fib_cache_helper(x - 1, cache) + fib_cache_helper(x - 2, cache)
        return cache[x]


def fib_loop(x):
    """Returns xth value in fibonacci sequence via iteration"""
    if x < 1:
        raise ValueError(errors[0])
    if x == 1:
        return 0
    else:
        a = 0
        b = 1
        for i in range(2, x):
            next_int = a + b
            a = b
            b = next_int
        return b


def fib_matrix(x):
    """Returns xth value in fibonacci sequence via matrix multiplication"""
    if x < 1:
        raise ValueError(errors[0])
    if x == 1:
        return 0
    else:
        m = [[1, 1], [1, 0]]  # magic matrix
        result = matrix_power(m, x - 2)
        return result[0][0]


def int_power(x, y):
    """Returns x^y via binary exponentiation"""
    if y < 0:
        raise ValueError(errors[1])
    binary_digits = base10_to_binary(y)
    binary_digits.reverse()
    product, i = 1, 1
    for digit in binary_digits:
        if digit:
            product *= int_power_brute(x, i)
        i *= 2
    return product


def int_power_brute(x, y):
    """Returns x^y via brute force"""
    if y < 0:
        raise ValueError(errors[1])
    product = 1
    for _ in range(y):
        product = product * x
    return product


def base10_to_binary(x):
    """Converts a base 10 integer to binary"""
    if x < 0:
        raise ValueError(errors[2])
    elif not isinstance(x, int):
        raise ValueError(errors[3])
    digits = []
    while x > 0:
        digits.insert(0, x % 2)
        x //= 2
    return digits


def matrix_multiply(m1, m2):
    """Multiplies two matrices together"""
    if len(m1[0]) != len(m2):
        return False
    return [[sum(a * b for a, b in zip(m1_row, m2_col)) for m2_col in zip(*m2)] for m1_row in m1]


def matrix_power(m, y):
    """Returns matrix raised to a power"""
    binary_digits = base10_to_binary(y)
    binary_digits.reverse()
    n = len(m)

    # Create the matrix equivalent to the integer 1
    identity_matrix = [[int(i == j) for i in range(n)] for j in range(n)]

    # Init final matrix with identity matrix
    product = identity_matrix

    # Loop through the binary digits
    for digit in binary_digits:

        # If the digit is a 1, multiply by the current matrix power
        if digit:
            product = matrix_multiply(product, m)

        # Square the matrix every time to increase the power
        m = matrix_multiply(m, m)

    return product


def matrix_print(m):
    """Prints a matrix"""
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(f"{m[i][j]} ", end="")
        print()

