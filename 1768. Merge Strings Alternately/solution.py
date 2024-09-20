class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ms = ''
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                ms += word1[i]
            if i < len(word2):
                ms += word2[i]
        print(ms)
        return ms           

Solution().mergeAlternately("ab", "pqrs")