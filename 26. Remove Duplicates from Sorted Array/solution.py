from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        found = []
        k = 0
        for i in range(len(nums)):
            if nums[i] not in found:
                nums[k] = nums[i]
                found.append(nums[i])
                k += 1

        return k