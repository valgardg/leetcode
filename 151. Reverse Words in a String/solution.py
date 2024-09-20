class Solution:
    def reverseWords(self, s: str) -> str:
        ss = s.split()
        print(ss)
        return ' '.join(ss[::-1])

# way too easy for a medium
print(Solution().reverseWords('the sky is blue'))