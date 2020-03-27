def join(separator: str):
    def _join(arr: list):
        return separator.join(arr)

    return _join

