import functools


def thrush(x, f):
    """
    Applies function M{f} to value M{x}
    @type x: Any
    @type f: function
    """
    return f(x)


def tap(f):
    """
    Calls function M{f} with value M{x}, then returns M{x}
    @type f: function
    @return: x
    """

    def _tap(x):
        f(x)
        return x

    return _tap


def pipe(*functions):
    """
    Performs right-to-left function composition, essentially creating a pipeline of functions.
    Each function in this pipeline will be called with the return value of the previous function.
    The first argument can take any number of parameters; the rest should be unary.
    @type functions: function
    @rtype: function
    """

    def _pipe(*args, **kwargs):
        return functools.reduce(thrush, functions[1:], functions[0](*args, **kwargs))

    return _pipe


def compose(*functions):
    """
    Performs left-to-right function composition.
    The last argument can take any number of arguments, but the rest should be unary.
    @type functions: function
    @rtype: function
    """
    return pipe(*reversed(functions))
