def find_rotate_index(nums):
    left = 0
    right = len(nums) - 1

    if nums[left] < nums[right]:
        return 0

    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] > nums[pivot + 1]:
            return pivot + 1
        else:
            if nums[pivot] < nums[left]:
                right = pivot - 1
            else:
                left = pivot + 1

print(find_rotate_index([6,7,8,1,2,3,4,5]))
