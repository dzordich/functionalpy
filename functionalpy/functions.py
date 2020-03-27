import functools
from typing import Tuple, List

from ._utils import _getparams
from ._types import Function, F1


def apply(f):
    """
    Applies function M{f} to argument list M{y}
    @type f: function
    """

    def _apply(y: List):
        return f(*y)

    return _apply


def thrush(x, f):
    """
    Applies function M{f} to value M{x}
    @type f: function
    """
    return f(x)


def tap(f):
    """
    Returns a function that when called with value M{x}, runs M{f} on M{x}, then returns M{x}
    @type f: function
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
    @type functions: (function)
    """

    def _pipe(*args, **kwargs):
        return functools.reduce(thrush, functions[1:], functions[0](*args, **kwargs))

    return _pipe


def compose(*fs: Tuple[Function, ...]) -> Function:
    """
    Performs left-to-right function composition.
    The last argument can take any number of arguments, but the rest should be unary.
    """
    return pipe(*reversed(fs))


def curry(f: Function):
    """

    @type f: function
    @rtype: function
    """

    def _curry(*args, **kwargs):
        if len(args) >= len(_getparams(f)):
            return f(*args, **kwargs)
        return curry(functools.partial(f, *args, **kwargs))

    return _curry


def add3(a, b, c=1):
    return a + b + c


addToOne = curry(add3)
print(addToOne(1))
