from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 1 if len(nums) > 0 else 0
        for num in nums:
            if num - 1 in nums:
                continue
            if num + 1 in nums:
                nlongest = 1
                cc = num
                while cc + 1 in nums:
                    nlongest += 1
                    if nlongest > longest:
                        longest = nlongest
                    cc +=  1
        return longest
            

print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2])) # 4
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 9
print(Solution().longestConsecutive([1,2,0,1])) # 3
print(Solution().longestConsecutive([0])) # 1
print(Solution().longestConsecutive([0,0])) # 1
print(Solution().longestConsecutive([])) # 0