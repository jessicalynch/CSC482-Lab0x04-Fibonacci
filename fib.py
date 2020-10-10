#!/usr/bin/env python3

errors = ["Error: sequence index must be 1 or greater"]


def fib_recur(x):
    """Returns the xth value of the fibonacci sequence via recursion"""
    if x < 1:
        raise ValueError(errors[0])
    elif x == 1 or x == 2:
        return x - 1
    else:
        return fib_recur(x - 1) + fib_recur(x - 2)


def fib_cache(x):
    if x < 1:
        raise ValueError(errors[0])
    else:
        cache = {}
        return fib_cache_helper(x - 1, cache)


def fib_cache_helper(x, cache):
    """Returns the xth value of the fibonacci sequence via recursion
    and a cache table to avoid duplicate calculations"""
    # print(x, cache)
    if x == 0 or x == 1:
        return x
    elif x in cache:
        return cache[x]
    else:
        cache[x] = fib_cache_helper(x - 1, cache) + fib_cache_helper(x - 2, cache)
        return cache[x]


def fib_loop(x):
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
    if x < 1:
        raise ValueError(errors[0])
    if x == 1:
        return 0
    else:
        m = [[1, 1], [1, 0]]  # magic matrix
        result = matrix_power(m, x - 2)
        return result[0][0]


def int_power(x, y):
    binary_digits = base10_to_binary(y)
    binary_digits.reverse()
    product, i = 1, 1
    for digit in binary_digits:
        if digit:
            product *= int_power_brute(x, i)
        i *= 2
    return product


def int_power_brute(x, y):
    product = 1
    for _ in range(y):
        product = product * x
    return product


def base10_to_binary(x):
    digits = []
    while x > 0:
        digits.insert(0, x % 2)
        x //= 2
    return digits


def matrix_multiply(m1, m2):
    if len(m1[0]) != len(m2):
        return False
    return [[sum(a * b for a, b in zip(m1_row, m2_col)) for m2_col in zip(*m2)] for m1_row in m1]


def matrix_power(m, y):
    binary_digits = base10_to_binary(y)
    binary_digits.reverse()
    n = len(m)
    identity_matrix = [[int(i == j) for i in range(n)] for j in range(n)]
    product = identity_matrix
    for digit in binary_digits:
        if digit:
            product = matrix_multiply(product, m)
        m = matrix_multiply(m, m)
    return product


def matrix_print(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(f"{m[i][j]} ", end="")
        print()

