class Solution:
    def removeStars(self, s: str) -> str:
        pp = 0
        
        while pp < len(s):
            if s[pp] == '*':
                s = s[:pp-1] + s[pp+1:]
                pp -= 2
            pp += 1

        return s

print(Solution().removeStars('leet**cod*e'))