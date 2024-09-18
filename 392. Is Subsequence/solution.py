class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        searchIndex = 0

        if s == "":
            return True

        for i in range(len(t)):
            if t[i] == s[searchIndex]:
                searchIndex += 1
            if searchIndex == len(s):
                return True
        return False

print(Solution().isSubsequence('abc', 'ahbgdc'))
print(Solution().isSubsequence('axc', 'ahbgdc'))
print(Solution().isSubsequence('aec', 'ahbgdc'))