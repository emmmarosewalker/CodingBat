# CodingBat
These are problems from the website codingbat.com. They are algorithmic problems with sets of test cases. 
For example:
```python
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
```

All tests passed before adding to git
