def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    return [str(bin(x)).count('1') for x in range(n + 1)]

print(countBits(5))
