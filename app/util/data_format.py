def int_or_none(x):
    """
    :rtype: int or None
    """
    if isinstance(x, int):
        return x
    else:
        return None


def str_or_none(s):
    """
    :rtype: str or None
    """
    if isinstance(s, str):
        return s
    else:
        return None


def to_int_or_minus_1(s):
    """
    :return: int(s) if OK. Otherwise, -1.
    :rtype: int
    """
    try:
        return int(s)
    except ValueError:
        return -1
