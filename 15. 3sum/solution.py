from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # we want to sort our list because that way we know left and right pointers point to lowest and highest possibilities
        # print(nums)
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                # print(f"Skipping i: {i}")
                continue
            lp = i + 1
            rp = len(nums) - 1
            while lp < rp:
                total = nums[i] + nums[lp] + nums[rp]
                
                if total > 0:
                    rp -= 1
                elif total < 0:
                    lp += 1
                elif total == 0:
                    res.append([nums[i], nums[lp], nums[rp]])
                    lp += 1
                    while lp > 0 and nums[lp] == nums[lp-1] and lp < rp:
                        lp += 1
        return res
                

print(Solution().threeSum([-1,0,1,2,-1,-4]))
print(Solution().threeSum([0,0,0,0]))
# print(Solution().threeSum([-2,-3,0,0,-2]))
print(Solution().threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))