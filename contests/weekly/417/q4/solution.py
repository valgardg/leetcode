
from typing import List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        chardict = {chr(i): chr((i - 97 + 1) % 26 + 97) for i in range(97, 123)}
        word = "a"
        c = 0
        while len(word) < k:
            if operations[c] == 0:
                word += word
            else:
                for char in word:
                    word += chardict[char]
            c += 1
        # print(word)
        return word[k-1]


print(Solution().kthCharacter(5, [0,0,0]))