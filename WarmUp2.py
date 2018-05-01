# Source of practice problems: http://codingbat.com/python/Warmup-2

def string_times(str, n):
    """
    :return: Given a string and a non-negative int n,
    return a larger string that is n copies of the original string.

    >>> string_times('Hi', 2)
    'HiHi'
    >>> string_times('Hi', 3)
    'HiHiHi'
    >>> string_times('Hi', 1)
    'Hi'
    """
    return str * n


def front_times(str, n):
    """ Given a string and a non-negative int n,
    we'll say that the front of the string is the first 3 chars,
    or whatever is there if the string is less than length 3.
    Return n copies of the front

    >>> front_times('Chocolate', 2)
    'ChoCho'
    >>> front_times('Chocolate', 3)
    'ChoChoCho'
    >>> front_times('Abc', 3)
    'AbcAbcAbc'
    """
    front = ""
    if len(str) <= 3:
        front = str
    else:
        front = str[0:3]
    return n * front


def string_bits(str):
    """ Given a string, return a new string made of every other char
    starting with the first, so "Hello" yields "Hlo".
    >>> string_bits('Hello')
    'Hlo'
    >>> string_bits('Hi')
    'H'
    >>> string_bits('Heeololeo')
    'Hello'
    """
    if len(str) <= 1:
        return str
    bits = str[0]
    i = 2
    while (i < len(str)):
        bits += str[i]
        i+= 2
    return bits


def string_splosion(str):
    """
    Given a non-empty string like "Code" return a string like "CCoCodCode".

    >>> string_splosion('Code')
    'CCoCodCode'
    >>> string_splosion('abc')
    'aababc'
    >>> string_splosion('ab')
    'aab'
    """
    length = len(str)
    i = 0
    newStr = ""
    while (i <= length):
        newStr += str[:i]
        i+=1
    return newStr


def last2(str):
    """
    Given a string, return the count of the number of times
    that a substring length 2 appears in the string and also
    as the last 2 chars of the string, so "hixxxhi" yields 1
    (we won't count the end substring).

    >>> last2('hixxhi')
    1
    >>> last2('xaxxaxaxx')
    1
    >>> last2('axxxaaxx')
    2
    """
    # Screen out too-short string case.
    if len(str) < 2:
        return 0

    # last 2 chars, can also be written as str[-2:]
    last2 = str[len(str) - 2:]
    count = 0

    # Check each substring length 2 starting at i
    for i in range(len(str) - 2):
        sub = str[i:i + 2]
        if sub == last2:
            count = count + 1

    return count


def array_count9(nums):
    """ Given an array of ints, return the number of
    9's in the array.

    array_count9([1, 2, 9])
    1
    array_count9([1, 9, 9])
    2
    array_count9([1, 9, 9, 3, 9])
    3
    """
    count = 0
    for i in range(len(nums)):
        if nums[i] == 9:
            count += 1
    return count


def array_front9(nums):
    """ Given an array of ints, return True if one of the first 4 elements
    in the array is a 9. The array length may be less than 4.

    >>> array_front9([1, 2, 9, 3, 4])
    True
    >>> array_front9([1, 2, 3, 4, 9])
    False
    >>> array_front9([1, 2, 3, 4, 5])
    False
    """
    if len(nums) <= 4:
        for num in nums:
            if num == 9:
                return True
        return False

    i = 0
    while i < 4:
        if nums[i] == 9:
            return True
        i += 1

    return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()