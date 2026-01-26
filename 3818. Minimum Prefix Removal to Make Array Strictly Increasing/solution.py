class Solution(object):
    def minimumPrefixLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                index = i
        
        return index
