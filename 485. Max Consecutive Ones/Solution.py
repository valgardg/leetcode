class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        maxcount = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            maxcount = max(maxcount, count)
        return maxcount
