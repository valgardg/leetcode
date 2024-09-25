from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp = 0
        rp = 0

        while rp < len(prices):
            profit = prices[rp] - prices[lp]
            if profit > max_profit:
                max_profit = profit
            if prices[rp] < prices[lp]:
                lp += 1
            else:
                rp += 1
            
        return max_profit

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([7,6,4,3,1]))