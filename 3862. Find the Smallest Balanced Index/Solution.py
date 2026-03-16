class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        pp = 1
        mx = 10**15
        prefix_products = []
        for i in range(len(nums)-1, -1, -1):
            pp = min(mx, pp * nums[i])
            prefix_products.append(pp)
        prefix_products = prefix_products[::-1]
        ps = 0
        for i in range(len(nums)):
            if i == len(nums) - 1:
                if ps == 1:
                    return i
                else:
                    return -1
            if ps == prefix_products[i+1]:
                return i
            ps += nums[i]
        return -1
