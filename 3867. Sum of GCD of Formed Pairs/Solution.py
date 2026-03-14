import math
class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxes = []
        prefixGcd = []
        for i, num in enumerate(nums):
            if maxes == []:
                maxes.append(num)
            else:
                maxes.append(max(num, maxes[i-1]))
            prefixGcd.append(math.gcd(nums[i], maxes[i]))

        # print(maxes)
        # print(prefixGcd)
        # print(sorted(prefixGcd))

        prefixGcd = sorted(prefixGcd)

        pair_gcd_sum = 0
        while len(prefixGcd) > 1:
            small = prefixGcd.pop(0)
            large = prefixGcd.pop(-1)
            pair_gcd_sum += math.gcd(small, large)
            # print(f'small: {small}, large: {large}, pair_sum: {pair_gcd_sum}, prefixGcd: {prefixGcd}')
        return pair_gcd_sum
