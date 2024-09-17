from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        finalList = []
        for i in range(len(nums)):
            total = None
            for l in range(len(nums)):
                if(l != i):
                    if(total == None):
                        total = nums[l]
                    else:
                        total *= nums[l]
            finalList.append(total)
        return finalList
                

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))
print(solution.productExceptSelf([-1,1,0,-3,3]))