#!/usr/bin/python3
import sys
from primality import is_prime

def factorize(num):
    return None, None

if __name__ == "__main__":
    num = str(sys.argv[1])
    primality = is_prime(num)
    if primality:
        print(num + " is a Prime Number.")
    else:
        factor1, factor2 = factorize(num)
