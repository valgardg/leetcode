from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = {}
        for no in arr:
            if no in occ:
                occ[no] += 1
            else:
                occ[no] = 0
        freqs = []
        for key in occ:
            if occ[key] in freqs:
                return False
            else:
                freqs.append(occ[key])
        return True

print(Solution().uniqueOccurrences([1,2,2,1,1,3]))