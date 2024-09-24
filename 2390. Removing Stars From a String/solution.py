class Solution:
    def removeStars(self, s: str) -> str:
        final = ''
        count = 0
        pp = 0

        for char in s:
            if char == '*':
                count += 1
        
        while count > 0:
            print(pp)
            if s[pp] == '*':
                s = s[:pp-1] + s[pp+1:]
                count -= 1
                pp -= 2
            pp += 1

        return s

print(Solution().removeStars('leet**cod*e'))