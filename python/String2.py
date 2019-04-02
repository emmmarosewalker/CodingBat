def double_char(str):
    """ Given a string, return a string where
     for every char in the original, there are two chars.

    >>> double_char('The')
    'TThhee'
    >>> double_char('AAbb')
    'AAAAbbbb'
    >>> double_char('Hi-There')
    'HHii--TThheerree'
     """
    new_string = ""
    for s in str:
        new_string += s*2

    return new_string


def count_hi(str):
    """ return number of times 'hi' appears in string
    >>> count_hi('abc hi ho')
    1
    >>> count_hi('ABChi hi')
    2
    >>> count_hi('hihi')
    2
    """
    return str.count('hi')


def cat_dog(str):
    """ Return True if the string "cat" and "dog" appear
    the same number of times in the given string.
    >>> cat_dog('catdog')
    True
    >>> cat_dog('catcat')
    False
    >>> cat_dog('1cat1cadodog')
    True
    """
    count_cat = str.count('cat')
    count_dog = str.count('dog')
    if count_cat == count_dog:
        return True
    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()