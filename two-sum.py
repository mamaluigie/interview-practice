def twoSum(nums, target):
    for x in range(len(nums)):
        for y in range(len(nums) - 1):
            if nums[y] + nums[x] == target and y != x:
                return [x, y]

        
        
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

print(twoSum([3,2,4], 6))
