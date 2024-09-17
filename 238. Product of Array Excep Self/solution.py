from typing import List

class Solution:
    def prefixArray(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        for i in range(2, len(nums)):
            pref[i] = pref[i-1] * nums[i-1]
            # print(f'i: {i}, pref[i-2]: {pref[i-1]}, nums[i-1]: {nums[i-1]}')
        print(f'prefix: {pref}')
        return pref

    def suffixArray(self, nums: List[int]) -> List[int]:
        suf = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]
        print(f'suffix: {suf}')
        return suf
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = self.prefixArray(nums)
        suf = self.suffixArray(nums)

        final = []
        for i in range(len(pref)):
            # print(f'pref[i]: {pref[i]}, suf[i]: {suf[i]}')
            final.append(pref[i] * suf[i])
        return final
                

solution = Solution()
# print(solution.prefixArray([1,2,3,4]))
# print(solution.suffixArray([1,2,3,4]))
print(solution.productExceptSelf([1,2,3,4]))
print(solution.productExceptSelf([-1,1,0,-3,3]))