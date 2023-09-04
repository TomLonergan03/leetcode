from functools import reduce


def lonelyinteger(a):
    return reduce(lambda x, y: x ^ y, a, 0)
