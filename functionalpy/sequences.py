from functools import reduce


def append(x, y):
    return x[:].append(y) if y else x


def listfrom(*values):
    return reduce(append, values, [])
