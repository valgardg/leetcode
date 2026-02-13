class Solution(object):
    def maximumStrongPairXor(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_xor = -1

        for i, num1 in enumerate(nums):
            for j in range(i, len(nums)):
                num2 = nums[j]
                isStrong = abs(num2 - num1) <= min(num1, num2)
                if isStrong:
                    xor = num1 ^ num2
                    if xor > max_xor:
                        max_xor = xor
        
        return max_xor
        
print(Solution().maximumStrongPairXor([1,2,3,4,5]))
