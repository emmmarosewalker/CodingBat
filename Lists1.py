# Source: http://codingbat.com/prob/p181624

def first_last6(nums):
    """
Given an array of ints, return True if 6
appears as either the first or last element
in the array. The array will be length 1 or more.
>>> first_last6([1, 2, 6])
True
>>> first_last6([6, 1, 2, 3])
True
>>> first_last6([13, 6, 1, 2, 3])
False
>>> first_last6([3])
False
>>> first_last6([1, 2, 3, 4, 6])
True
"""
    if len(nums) == 1:
        if nums.count(6) > 0:
            return True
        else:
            return False
    if nums.pop(0) == 6 or nums.pop(len(nums)-1) == 6:
        return True
    else:
        return False


def same_first_last(nums):
    """Given an array of ints, return True if the
    array is length 1 or more, and the first element and the
    last element are equal.
    >>> same_first_last([1, 2, 3])
    False
    >>> same_first_last([1, 2, 3, 1])
    True
    >>> same_first_last([1, 2, 1])
    True
    """
    if len(nums) < 1:
        return False
    elif len(nums) == 1:
        return True
    first = nums[0]
    last = nums[len(nums)-1]
    if first == last:
        return True
    return False


def make_pi():
    """
    Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
    >>> make_pi()
    [3, 1, 4]
    """
    import math
    my_pi = round(math.pi * 100)
    pi_list = [int(num) for num in str(my_pi)]
    return pi_list


def common_end(a,b):
    """Given 2 arrays of ints, a and b, return True if
    they have the same first element or they have the same
    last element. Both arrays will be length 1 or more.
    >>> common_end([1, 2, 3], [7, 3])
    True
    >>> common_end([1, 2, 3], [7, 3, 2])
    False
    >>> common_end([1, 2, 3], [1, 3])
    True
    """
    # Check if both have one element and whether it is the same
    if len(a) == 1 and len(b) == 1:
        if a[0] == b[0]:
            return True
        else:
            return False

    # Check if both have the same first element or last element
    if a[0] == b[0] or a[len(a)-1] == b[len(b)-1]:
        return True
    else:
        return False


def sum3(nums):
    """Given an array of ints length 3, return the
    sum of all the elements.
    >>> sum3([1, 2, 3])
    6
    >>> sum3([5, 11, 2])
    18
    >>> sum3([7, 0, 0])
    7
    """
    count = 0
    for num in nums:
        count += num
    return count


def rotate_left3(nums):
    """Given an array of ints length 3, return an array with the
    elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
    >>> rotate_left3([1, 2, 3])
    [2, 3, 1]
    >>> rotate_left3([5, 11, 9])
    [11, 9, 5]
    >>> rotate_left3([7, 0, 0])
    [0, 0, 7]
    """
    rotated_list = nums[1:len(nums)]
    rotated_list.append(nums[0])
    return rotated_list

if __name__ == '__main__':
    import doctest
    doctest.testmod()