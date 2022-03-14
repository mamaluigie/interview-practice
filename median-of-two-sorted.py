import math
import pdb

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    def merge(arr1, arr2):
        new_arr = []
        for x in arr1:
            for y in arr2:
                if x > y:
                    new_arr.append(y)
                    new_arr.append(x)
                else:
                    new_arr.append(x)
                    new_arr.append(y)   
        return new_arr
    
    merged_arr = merge(nums1, nums2)
    pdb.set_trace()
    return merged_arr[len(merged_arr) // 2] if len(merged_arr) % 2 == 0 else merged_arr[len(merged_arr // 2)] / merged_arr[math.ceil(len(merged_arr) / 2)]

print(findMedianSortedArrays([1,2], [3,4]))
