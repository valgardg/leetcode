from typing import List
from collections import Counter
class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        arr = []

        required = Counter(word2)
        existing = {}

        lp = 0
        rp = 0

        return arr

print(Solution().validSequence("vbcca", "abc"))