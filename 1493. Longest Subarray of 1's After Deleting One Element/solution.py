from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        k = 1
        lp = 0
        rp = 0
        
        flipped = []

        max_count = 0

        while rp < len(nums):
            if nums[rp] == 1:
                rp +=1
            else:
                if len(flipped) < k and k > 0:
                    flipped.append(rp)
                    rp += 1
                else:
                    if k == 0:
                        rp += 1
                        lp = rp
                    else:    
                        lp = flipped.pop(0)
                        lp += 1

            # print(f'checking {nums[lp:rp]}, flipped: {flipped}, length = {rp-lp}')
            length = rp - lp
            if length > max_count:
                max_count = length
            
        return max_count - 1

# print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
# print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
print(Solution().longestSubarray([1,1,0,1]))
print(Solution().longestSubarray([0,1,1,1,0,1,1,0,1]))
print(Solution().longestSubarray([1,1,1]))
