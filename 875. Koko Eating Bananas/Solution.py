import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def hours_to_eat_at_k(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/k)
            return hours

        # print(hours_to_eat_at_k(4))

        l, r = 1, max(piles)
        while l < r:
            # print(f'l: {l}, r: {r}, m: {l + (r-l) // 2}, hours_to_eat_at_k(m): {hours_to_eat_at_k(l + (r-l) // 2)}')
            m = l + (r-l) // 2
            if hours_to_eat_at_k(m) <= h:
                r = m
            else:
                l = m + 1
        return l
