from typing import List
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        h = {}
        count = 0
        for i in range(len(nums)):
            needed = k-nums[i]
            if needed in h:
                # print(f'{needed}(index {h[needed]}) and {nums[i]} summed would equal {k}')
                del h[needed]
                count += 1
            else:
                h[nums[i]] = i
        print(f'{count}\n')
        return count

Solution().maxOperations([1,2,3,4], 5)
Solution().maxOperations([3,1,3,4,3], 6)
# Solution().maxOperations([2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], 3)