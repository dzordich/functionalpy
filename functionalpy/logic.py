negate = lambda f: lambda x: not bool(f(x))


def disjunct(f1, f2):
    def _disjunct(x):
        return bool(f1(x) or f2(x))

    return _disjunct


def conjunct(f1, f2):
    def _conjunct(x):
        return bool(f1(x) and f2(x))

    return _conjunct


def xor(f1, f2):
    return conjunct(negate(conjunct(f1, f2)), disjunct(f1, f2))
