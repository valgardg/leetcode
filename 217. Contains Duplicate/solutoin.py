from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        vals = {}
        for num in nums:
            if num in vals:
                return True
            vals[num] = num
        return False