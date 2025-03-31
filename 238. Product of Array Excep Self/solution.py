from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preff = [1]
        suff = [1]

        rvp = 1
        rvs = 1

        for i in range(len(nums)-1):
            rvp = rvp * nums[i]
            preff.append(rvp)
            rvs = rvs * nums[len(nums)-i-1]
            suff.append(rvs)

        return [preff[i] * suff[len(suff) - i -1] for i in range(len(suff))]


solution = Solution()
# print(solution.prefixArray([1,2,3,4]))
# print(solution.suffixArray([1,2,3,4]))
# print(solution.prefixArray([-1,1,0,-3,3]))
# print(solution.suffixArray([-1,1,0,-3,3]))
print(solution.productExceptSelf([1,2,3,4]))
print(solution.productExceptSelf([-1,1,0,-3,3]))
