#!/usr/bin/env python3

try:
    print("Enter the first number:")
    n1_str = input()
    n1 = int(n1_str)

    print("Enter the second number:")
    n2_str = input()
    n2 = int(n2_str)

    res = n1 * n2

    print(f"{n1} x {n2} = {res}")

    if res > 0:
        print("The result is positive.")
    elif res < 0:
        print("The result is negative.")
    else:
        print("The result is positive and negative")
except EOFError:
    pass
except ValueError:
    pass
