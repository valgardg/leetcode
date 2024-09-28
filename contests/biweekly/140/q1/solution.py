from typing import List
class Solution:
    def minElement(self, nums: List[int]) -> int:
        minel = float('inf')
        for num in nums:
            n = sum([int(char) for char in str(num)])
            if n < minel:
                minel = n
        return minel


print(Solution().minElement([999,19,199]))