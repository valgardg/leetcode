class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return nums[0]
        mem = {0: nums[0], 1: max(nums[0], nums[1])}

        def robr(n):
            if n in mem:
                return mem[n]
            mem[n] = max(robr(n-1), nums[n] + robr(n-2))
            # print(f'self.mem[{n}] = {self.mem[n]}')
            # print(f'self.mem: {self.mem}')
            return mem[n]

        maxrob = 0
        for i, num in enumerate(nums):
            # print(f'checking i: {i}, num: {num}')
            maxrob = max(maxrob, robr(i))
        return maxrob

print(Solution().rob([1,2,3,1]))
# print(Solution().rob([2,7,9,3,1]))
