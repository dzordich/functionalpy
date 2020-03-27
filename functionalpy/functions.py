import functools
from typing import Iterable, List

from ._utils import _getparams
from ._types import F, F1


def _curryN(arity):
    """
    @param arity: number of arguments to take before evaluating
    @type arity: int
    """

    def _curry(f: F) -> F1:
        def _curried(*args, **kwargs):
            new_arity = arity - len(args)
            if new_arity <= 0:
                return f(*args, **kwargs)
            return _curryN(new_arity)(functools.partial(f, *args, **kwargs))

        return _curried

    return _curry


def _apply(f, y: Iterable):
    """
    Applies function M{f} to argument list M{y}
    """
    return f(*y)


def apply(f):
    """
    Returns a function that when called with argument list M{y},
    applies M{y} to M{f}.
    @type f: function
    """

    def _ap(y: List):
        return _apply(f, y)

    return _ap


def thrush(x, f):
    """
    Applies function M{f} to value M{x}
    @type x: Any
    @type f: function
    @rtype: Any
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


def pipe(*fns):
    """
    Performs right-to-left function composition, essentially creating a pipeline of fns.
    Each function in this pipeline will be called with the return value of the previous function.
    The first argument can take any number of parameters; the rest should be unary.
    @type fns: function
    @rtype: function
    """

    def _pipe(*args, **kwargs):
        return functools.reduce(thrush, fns[1:], fns[0](*args, **kwargs))

    return _pipe


def compose(*fns):
    """
    Performs left-to-right function composition.
    The last argument can take any number of arguments, but the rest should be unary.
    @type fns: function
    @rtype: function
    """
    return _apply(pipe, reversed(fns))


def curry(f: F) -> F1:
    """
    Creates a new, curried version of a function.
    A curried function allows you to pass in arguments one at a time;
    it will not evaluate until all it's positional arguments are satisfied.
    @type f: function
    @rtype: function
    """

    def _curry(*args, **kwargs):
        if len(args) >= len(_getparams(f)):
            return f(*args, **kwargs)
        return curry(functools.partial(f, *args, **kwargs))

    return _curry
