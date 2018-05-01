def count_evens(nums):
    """Return the number of even ints in the given array.
    >>> count_evens([2, 1, 2, 3, 4])
    3
    >>> count_evens([2, 2, 0])
    3
    >>> count_evens([1, 3, 5])
    0
    """
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count


def big_diff(nums):
    """Given an array length 1 or more of ints, return the
    difference between the largest and smallest values in the array.
    Note: the built-in min(v1, v2) and max(v1, v2) functions return the
    smaller or larger of two values.
    >>> big_diff([10, 3, 5, 6])
    7
    >>> big_diff([7, 2, 10, 9])
    8
    >>> big_diff([2, 10, 7, 2])
    8
    """
    big = nums[0]
    little = nums[0]
    for num in nums:
        if num > big:
            big = num
        elif num < little:
            little = num

    diff = big - little
    return diff


def centered_average(nums):
    """
Return the "centered" average of an array of ints,
which we'll say is the mean average of the values, except
ignoring the largest and smallest values in the array.
If there are multiple copies of the smallest value,
ignore just one copy, and likewise for the largest value.
Use int division to produce the final average. You may
assume that the array is length 3 or more.
    >>> centered_average([1, 2, 3, 4, 100])
    3
    >>> centered_average([1, 1, 5, 5, 10, 8, 7])
    5
    >>> centered_average([-10, -4, -2, -4, -2, 0])
    -3
"""
    # first sort the list
    nums.sort()
    # remove biggest and smallest
    nums = nums[1:len(nums)-1]
    # sum the numbers
    sum = 0
    for num in nums:
        sum += num
    average = int(sum/len(nums))
    return average


def sum13(nums):
    """ Return the sum of the numbers in the array,
    returning 0 for an empty array. Except the number 13
    is very unlucky, so it does not count and numbers
    that come immediately after a 13 also do not count.
    >>> sum13([1, 2, 2, 1])
    6
    >>> sum13([1, 1])
    2
    >>> sum13([1, 2, 2, 1, 13])
    6
    """
    # check if empty list
    if len(nums) == 0:
        return 0

    sum = 0
    i = 0
    while i < len(nums):
        # if the current num is 13, sum doesn't get added to. We increment i and continue.
        if nums[i] == 13:
            i += 1
            continue
        # also, if we're not at index 0, and the prev num is 13,
        # sum isn't added to. i is incremented and we continue.
        if i > 0 and nums[i-1] == 13:
            i += 1
            continue
        sum += nums[i]
        i += 1

    return sum


def sum67(nums):
    """
Return the sum of the numbers in the array,
except ignore sections of numbers starting with a 6 and
extending to the next 7 (every 6 will be followed by
at least one 7). Return 0 for no numbers.
 >>> sum67([1, 2, 2])
 5
>>> sum67([1, 2, 2, 6, 99, 99, 7])
5
>>> sum67([1, 1, 6, 7, 2])
4
 """
    # return 0 for no numbers
    if len(nums) == 0:
        return 0
    # find 6:

    i = 0
    sum = 0
    while i < len(nums):
        if nums[i] == 6:
            for num in range(i, nums.index(7,i)):
                i += 1
                continue
            i += 1
            continue
        sum += nums[i]
        i+= 1

    return sum


def has22(nums):
    """ Given an array of ints, return
    True if the array contains a 2 next to a 2 somewhere.

    >>> has22([1, 2, 2])
    True
    >>> has22([4, 5, 4])
    False
    >>> has22([2, 1, 2])
    False
    >>> has22([4, 2, 4, 2, 2, 5])
    True
    """
    list_strings = [str(num) for num in nums]
    joined_str = ""
    for snum in list_strings:
        joined_str += snum

    if "22" in joined_str:
        return True
    else:
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()