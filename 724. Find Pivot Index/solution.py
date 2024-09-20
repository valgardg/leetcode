from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # print(nums[:i], nums[i+1:])
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1
            
print(Solution().pivotIndex([1,7,3,6,5,6]))
print(Solution().pivotIndex([1,2,3]))
print(Solution().pivotIndex([2,1,-1]))