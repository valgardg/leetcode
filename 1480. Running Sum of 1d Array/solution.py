class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        running_sum = []
        prefix = 0
        for num in nums:
            prefix += num
            running_sum.append(prefix)
        
        return running_sum

print(Solution().runningSum([1,2,3,4]))