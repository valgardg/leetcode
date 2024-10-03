from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fd = {}
        for num in nums:
            if num in fd:
                fd[num] += 1
            else:
                fd[num] = 1
            val = fd[num]
        print(fd)
        sfd = sorted(fd.items(), key=lambda x: x[1], reverse=True)
        print(sfd)
        for item in sfd[:k]:
            print(item[0])
        return [item[0] for item in sfd[:k]]

print(Solution().topKFrequent([1,1,1,2,2,3], 2))