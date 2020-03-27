from functools import reduce


def append(x, y):
    """
    Appends M{y} to M{x}
    @type x: list
    @type y: Any
    @return: A new list created by appending y to x
    @rtype: list
    """
    return x[:].append(y) if y is not None else x


def listfrom(*values):
    """
    Creates a list from the arguments passed in
    """
    return reduce(append, values, [])
