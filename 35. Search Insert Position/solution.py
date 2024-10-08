from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums)-1
        m = (rp + lp) // 2
        while True:
            if nums[m] < target:
                lp = m
            elif nums[m] > target:
                rp = m
            elif nums[m] == target:
                return m
            m = (rp + lp) // 2
            if lp+1 == rp or lp == rp:
                # print(f'pointers: {lp} - {rp}')
                if target > nums[rp]:
                    return rp + 1
                if target > nums[lp]:
                    return lp + 1
                else:
                    return lp
            
print(f'Solved: {Solution().searchInsert([1,3,5,6], 5)}') # 2
print(f'Solved: {Solution().searchInsert([1,3,5,6], 2)}') # 1
print(f'Solved: {Solution().searchInsert([1,3,5,6], 7)}') # 4
print(f'Solved: {Solution().searchInsert([1,3,5,6], 0)}') # 0
print(f'Solved: {Solution().searchInsert([1], 0)}') # 0