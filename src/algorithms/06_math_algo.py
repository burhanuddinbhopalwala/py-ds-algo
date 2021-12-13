import pdb
import math

DEC_BASE = 10


def is_lucky(num):
    l = [0] * DEC_BASE
    while num > 0:
        q = num % 10
        if l[q] > 0:
            return False
        l[q] += 1
        num //= 10
    return True


# print(is_lucky(123456))  # * True
# print(is_lucky(375746))  # * False
################################################################################


def is_prime(num):
    for ele in range(2, math.floor(math.sqrt(num)) + 1):
        if num % ele:
            continue
        else:
            return False
    return True


# print(is_prime(13))
# * T.C. = O(sqrt(n))
################################################################################


def print_prime(n):
    prime = [True] * (n + 1)
    prime[0] = False
    prime[1] = False
    for ele in range(2, n+1):
        if prime[ele]:
            temp = ele * 2
            while temp < n+1:
                prime[temp] = False
                temp += ele

    for ele in range(n):
        if prime[ele]:
            print(ele)


print_prime(99)
# * T.C. =  < O(n * sqrt(n))
################################################################################
