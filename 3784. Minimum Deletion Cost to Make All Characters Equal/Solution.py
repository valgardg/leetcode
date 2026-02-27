from collections import defaultdict
class Solution(object):
    def minCost(self, s, cost):
        """
        :type s: str
        :type cost: List[int]
        :rtype: int
        """
        ind_costs = defaultdict(int)
        total_cost = 0
        for char, charcost in zip(s, cost):
            ind_costs[char] += charcost
            total_cost += charcost
        cost_to_remain = defaultdict(int)
        lowest_cost = float('inf')
        for char in s:
            char_cost = total_cost - ind_costs[char]
            if char_cost < lowest_cost:
                lowest_cost = char_cost
        return lowest_cost
