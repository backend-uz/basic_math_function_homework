def main(a, b):
    from math import floor
    '''find the floor division of a and b and return it.
    Args:
        a (int): a number
        b (int): a number
    Returns:
        int: the result.
    '''
    c = floor(a/b)
    return c
print(main(11, 2))
