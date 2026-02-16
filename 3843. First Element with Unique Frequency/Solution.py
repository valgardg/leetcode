from collections import defaultdict
class Solution(object):
    def firstUniqueFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_freq = defaultdict(int)
        freq_freq = defaultdict(int)
        for num in nums:
            num_freq[num] += 1
        
        for num, freq in num_freq.items():
            freq_freq[freq] += 1
        
        for num in nums:
            if freq_freq[num_freq[num]] == 1:
                return num
            
        return -1
        

print(Solution().firstUniqueFreq([20,10,30,30]))
print(Solution().firstUniqueFreq([20,20,10,30,30,30]))
print(Solution().firstUniqueFreq([10, 10, 20, 20]))
