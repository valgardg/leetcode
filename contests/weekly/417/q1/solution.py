
class Solution:
    def kthCharacter(self, k: int) -> str:
        chardict = {chr(i): chr((i - 97 + 1) % 26 + 97) for i in range(97, 123)}
        word = "a"
        while len(word) < k:
            gen = ''.join([chardict[char] for char in word])
            word += gen
        # print(word)
        return word[k-1]


print(Solution().kthCharacter(10))