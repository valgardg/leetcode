from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        exces = 0
        for i in range(len(nums)):
            if(exces):
                i -= 1
            print(f'i running for value {i}')
            if nums[i] == 0:
                for c in range(i, (len(nums) - i) -1):
                    nums[c] = nums[c+1]
                nums[-1] = 0
                exces += 1
            print(f'nums after iteration: {nums}, i: {i}')

        print(f'final nums: {nums}')