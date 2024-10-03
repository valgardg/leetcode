from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ad = {}
        for s in strs:
            if str(sorted(s)) in ad:
                ad[str(sorted(s))].append(s)
            else:
                ad[str(sorted(s))] = [s]
        
        return ad.values()
    
print(Solution().groupAnagrams(['eat','tea','tan','ate','nat','bat']))
print(Solution().groupAnagrams(['']))