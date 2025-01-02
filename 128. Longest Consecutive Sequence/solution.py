from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ht = {}
        for i in nums:
            if i not in ht:
                ht[i] = i
        # print(ht)
        longest = 0
        for i in ht.keys():
            # print(f'Checking {i}')
            cc = 1
            p = ht[i]
            while p-1 in ht:
                # print(f'Tunneling {p-1}')
                cc += 1
                p = ht[p-1]
            # print(f'cc: {cc}')
            if cc > longest:
                longest = cc

        return longest

print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2])) # 4
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 4
print(Solution().longestConsecutive([1,2,0,1])) # 4
print(Solution().longestConsecutive([0])) # 4
print(Solution().longestConsecutive([0,0])) # 4
print(Solution().longestConsecutive([])) # 4