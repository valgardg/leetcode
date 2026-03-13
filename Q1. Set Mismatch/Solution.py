class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prev = -1
        nums = sorted(nums)
        dup = None
        for num in nums:
            if num == prev:
                dup = num
                break
            else:
                prev = num
        for i in range(1, nums[-1]+2):
            if i not in nums:
                return [dup, i]
