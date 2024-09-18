from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroIndex = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroIndex] = nums[i]
                lastNonZeroIndex +=1
            
        for i in range(lastNonZeroIndex, len(nums)):
            nums[i] = 0
            
        print(nums)

# Solution().moveZeroes([0,0,1])
Solution().moveZeroes([0,1,0,0,0,3,12])