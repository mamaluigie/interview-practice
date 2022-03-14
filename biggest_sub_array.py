def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    total_sum = nums[0]
    L_slider = 0
    for i in range(1, len(nums)):
        if nums[i] + total_sum > total_sum:
            total_sum = nums[i] + total_sum 
        elif total_sum - nums[L_slider] > total_sum:
            total_sum = nums[L_slider] - total_sum 
            L_slider += 1

            
    return total_sum
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
