import inspect


def _getparams(f):
    return [
        param
        for param in inspect.signature(f).parameters.values()
        if param.default == inspect.Parameter.empty
    ]
