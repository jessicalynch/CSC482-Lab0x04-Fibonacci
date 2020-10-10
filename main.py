#!/usr/bin/env python3

import fib


def main():
    x = 25
    try:
        for i in range(1, x + 1):
            print(fib.fib_cache(i), end=" ")
        print()
        print("fib recur:", fib.fib_recur(x))
        print("fib cache:", fib.fib_cache(x))
        print("fib loop:", fib.fib_loop(x))
        print("fib matrix:", fib.fib_matrix(x))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
