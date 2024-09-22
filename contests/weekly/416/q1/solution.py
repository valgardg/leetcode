from typing import List

class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        count = 0
        bannedWords = set(bannedWords)
        for word in message:
            if word in bannedWords:
                count +=1
            if count > 1:
                return True
        return False

print(Solution().reportSpam(["leetcode", "leetcode","leetcode","world", "world"], ["world","hello"]))