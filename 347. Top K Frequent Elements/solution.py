from typing import List
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = defaultdict(int)
        for num in nums:
            tracker[num] += 1
        stracker = sorted(tracker.items(), key=lambda item: item[1], reverse=True)
        return [key for key,_ in stracker[:k]]
# print(Solution().topKFrequent([1,1,1,2,2,3], 2))
# print(Solution().topKFrequent([3,0,1,0], 1))
print(Solution().topKFrequent([4,1,-1,2,-1,2,3], 2))
