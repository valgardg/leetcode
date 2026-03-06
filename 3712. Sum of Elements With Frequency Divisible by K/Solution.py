from collections import defaultdict
class Solution(object):
    def sumDivisibleByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        totalsum = 0
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        for num, freq in freqs.items():
            if freq % k == 0:
                totalsum += num * freq
        return totalsum
