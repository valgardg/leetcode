from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        og = defaultdict(int)

        for i in range(len(s)):
            og_char = s[i]
            other_char = t[i]

            og[og_char] += 1
            og[other_char] -= 1

        for key in og.keys():
            if og[key] != 0:
                return False
        return True


print(Solution().isAnagram("catt", "tcat"))
