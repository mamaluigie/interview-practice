def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    s = set()
    for x in nums:
        if x not in s:
            s.add(x)
        else:
            return True
    return False

