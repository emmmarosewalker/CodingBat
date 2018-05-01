def sleep_in(weekday, vacation):
    """The parameter weekday is True if it is a weekday, and the parameter vacation
    is True if we are on vacation. We sleep in if it is not a weekday or
    we're on vacation. Return True if we sleep in.
    >>> sleep_in(False, False)
    True
    >>> sleep_in(True, False)
    False
    >>> sleep_in(False, True)
    True
    >>> sleep_in(True, True)
    True
    """

    if not weekday or vacation:
        return True
    else:
        return False


def monkey_trouble(a_smile, b_smile):
    """We have two monkeys, a and b, and the parameters a_smile and b_smile indicate
    if each is smiling. We are in trouble if they are both smiling or if neither of
    them is smiling. Return True if we are in trouble

    :param a_smile: True if monkey a is smiling, False if not
    :param b_smile: True if monkey b is smiling, False if not
    :return: We are in trouble if they are both smiling or if neither of
    them is smiling. Return True if we are in trouble
    >>> monkey_trouble(True, True)
    True
    >>> monkey_trouble(False, False)
    True
    >>> monkey_trouble(True, False)
    False
    """

    if (a_smile and b_smile) or (not a_smile and not b_smile):
        return True
    else:
        return False


def sum_double(a, b):
    """
    :param a: An int value
    :param b: An int value
    :return: Their sum, unless the two values are equal, return double their sum
    >>> sum_double(1, 2)
    3
    >>> sum_double(3, 2)
    5
    >>> sum_double(2, 2)
    8
    """
    if a == b:
        return 2 * (a + b)
    else:
        return a + b


def diff21(n):
    """
    :param n: An int value
    :return: The absolute difference between n and 21, except return double the absolute difference if n is over 21.
    >>> diff21(19)
    2
    >>> diff21(10)
    11
    >>> diff21(21)
    0
    """
    if n < 21:
        return abs(21 - n)
    else:
        return 2 * abs(21 - n)


def parrot_trouble(talking, hour):
    """
    :param talking: Boolean - whether or not the parrot is talking
    :param hour: the current hour in 24 hour time (range 0..23)
    :return: We are in trouble if the parrot is talking and the hour is
    before 7 or after 20. Return True if we are in trouble.
    >>> parrot_trouble(True, 6)
    True
    >>> parrot_trouble(True, 7)
    False
    >>> parrot_trouble(False, 6)
    False
    """
    if (talking and hour < 7) or (talking and hour > 20):
        return True
    else:
        return False


def makes10(a, b):
    """
    :param a: an int value
    :param b: an int value
    :return: return True if param a or param b is 10 or if their sum is 10.
    >>> makes10(9, 10)
    True
    >>> makes10(9, 9)
    False
    >>> makes10(1, 9)
    True
    """
    if a == 10 or b == 10 or a + b == 10:
        return True
    else:
        return False


def near_hundred(n):
    """
    :param n: an int value
    :return: True if param n is within 10 of 100 or 200, False if not.
    >>> near_hundred(93)
    True
    >>> near_hundred(90)
    True
    >>> near_hundred(89)
    False
    """
    if abs(100 - n) <= 10 or abs(200 - n) <= 10:
        return True
    else:
        return False


def pos_neg(a, b, negative):
    """

    :param a: an int value
    :param b: an int value
    :param negative: a boolean value
    :return: True if one is negative and one is positive.
    Except if the parameter "negative" is True, then return
    True only if both are negative.
    >>> pos_neg(1, -1, False)
    True
    >>> pos_neg(-1, 1, False)
    True
    >>> pos_neg(-4, -5, True)
    True
    """
    if (not negative and a >= 0 and b < 0) or (not negative and b >= 0 and a < 0):
        return True
    elif negative and a < 0 and b < 0:
        return True
    else:
        return False


def not_string(str):
    """
    :param str: A string
    :return:
    Given a string, return a new string where "not " has
    been added to the front. However, if the string already begins with
    "not", return the string unchanged.
    >>> not_string('candy')
    'not candy'
    >>> not_string('x')
    'not x'
    >>> not_string('not bad')
    'not bad'
    """
    # check for empty string and return straight away
    if len(str) == 0:
        return
    if str[0:3] == "not":
        return str
    else:
        return "not " + str


def missing_char(str, n):
    """
    :param str: a non-empty string
    :param n: an int - the index of a char in str
    :return: a new string where the char at index n has been removed.
    The value of n will be a valid index of a char in the original string
    (i.e. n will be in the range 0..len(str)-1 inclusive).
    >>> missing_char('kitten', 1)
    'ktten'
    >>> missing_char('kitten', 0)
    'itten'
    >>> missing_char('kitten', 4)
    'kittn'
    """
    leftStr = str[0:n]
    rightStr = str[n+1:]
    return leftStr + rightStr


def front_back(str):
    """
    :param str: a string
    :return: Given a string, return a new string
    where the first and last chars have been exchanged.
    >>> front_back('code')
    'eodc'
    >>> front_back('a')
    'a'
    >>> front_back('ab')
    'ba'
    """
    if len(str) <= 1:
        return str
    else:
        firstChar = str[0]
        lastChar = str[-1]
        middleChars = str[1:-1]
        return lastChar + middleChars + firstChar

def front3(str):
    """
    :param str:
    :return: Given a string, we'll say that the front is the first 3 chars of
    the string. If the string length is less than 3, the front is whatever is
    there. Return a new string which is 3 copies of the front.
    >>> front3('Java')
    'JavJavJav'
    >>> front3('Chocolate')
    'ChoChoCho'
    >>> front3('abc')
    'abcabcabc'
    """
    front = ""
    if len(str) <= 3:
        front = str
    else:
        front = str[0:3]
    return front * 3



if __name__ == '__main__':
    import doctest
    doctest.testmod()