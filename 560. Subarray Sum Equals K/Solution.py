from collections import defaultdict
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ps = 0
        total = 0
        freqs = defaultdict(int)
        nums = [0] + nums
        for p in nums:
            ps += p
            diff = ps - k
            total += freqs[diff]
            freqs[ps] += 1

        return total
