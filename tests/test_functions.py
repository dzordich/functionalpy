import pytest

from functionalpy import functions as FP
from inspect import signature


def test_pipe():
    square = lambda x: x * x
    add1 = lambda x: x + 1
    p = FP.pipe(square, add1)

    assert callable(p)
    assert p(2) == 5

    with pytest.raises(TypeError):
        p()
    with pytest.raises(TypeError):
        p(1, 2)


def test_pipe_2_args():
    add = lambda x, y: x + y
    square = lambda x: x * x

    p = FP.pipe(add, square)

    assert p(2, 3) == 25


class TestApply:
    def test_apply_is_curried(self):
        add3 = lambda x, y, z: x + y + z
        ap = FP.apply(add3)
        assert callable(ap)
        assert ap([1, 2, 3]) == 6
        with pytest.raises(TypeError):
            ap([1, 2])
        with pytest.raises(TypeError):
            ap()


class TestCompose:
    def test_with_method(self):
        obj = dict(a=1)
        c = FP.compose(lambda x: x + 1, obj.get)
        assert c("a") == 2
