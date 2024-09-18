from typing import List

class Solution:
    def prefixArray(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        for i in range(1, len(nums)):
            pref[i] = pref[i-1] * nums[i-1]
            print(f'i: {i}, pref[i-2]: {pref[i-1]}, nums[i-1]: {nums[i-1]}')
        print(f'prefix: {pref}')
        return pref

    def suffixArray(self, nums: List[int]) -> List[int]:
        suf = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]
            print(f'i: {i}, suf[i+1]: {suf[i+1]}, nums[i+1]: {nums[i+1]}')
        print(f'suffix: {suf}')
        return suf
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1] * len(nums)
        suf = [1] * len(nums)
        final = [1] * len(nums)
        for i in range(1, len(nums)):
            suf_index = abs(i-(len(nums))+1)
            # print(f'i/suf_index: {i} / {suf_index}')
            pref[i] = pref[i-1] * nums[i-1]
            suf[suf_index] = suf[suf_index+1] * nums[suf_index+1]
        
        # print(f'i: {i}\npref:{pref}\nsuf:{suf}')
        for i in range(len(final)):
            final[i] = pref[i] * suf[i]

        return final
                

solution = Solution()
# print(solution.prefixArray([1,2,3,4]))
# print(solution.suffixArray([1,2,3,4]))
# print(solution.prefixArray([-1,1,0,-3,3]))
# print(solution.suffixArray([-1,1,0,-3,3]))
print(solution.productExceptSelf([1,2,3,4]))
print(solution.productExceptSelf([-1,1,0,-3,3]))