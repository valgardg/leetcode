from collections import defaultdict
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        positions = defaultdict(list)
        final = {}
        for i in range(len(temperatures)):
            temp = temperatures[i]
            positions[temp].append(i)
            
            while len(stack) > 0 and temp > stack[-1]:
                popped = stack.pop()
                poppeed_position = positions[popped].pop()
                final[poppeed_position] = i - poppeed_position

            stack.append(temp)

        # print(stack)
        # print(positions)
        # print(final)

        for n in stack:
            while len(positions[n]) > 0:
                position = positions[n].pop()
                final[position] = 0

        return list(dict(sorted(final.items())).values())


# print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
# print(Solution().dailyTemperatures([30,60,90]))
print(Solution().dailyTemperatures([34,80,80,34,34,80,80,80,80,34]))