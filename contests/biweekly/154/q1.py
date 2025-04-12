from typing import List
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        min_no = 0
        removal_index = 0
        
        while sum(nums) % k != 0:
            if nums[removal_index] > 0:
                nums[removal_index] -= 1
                min_no += 1
            else:
                removal_index += 1
        
        return min_no
