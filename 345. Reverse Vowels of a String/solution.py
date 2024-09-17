class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        foundVowels = [char for char in s if char.lower() in vowels]
        vowelIndex = 1
        finalString = ''
        for char in s:
            if(char.lower() not in vowels):
                finalString += char
            else:
                finalString += foundVowels[-1 * vowelIndex]
                vowelIndex += 1
        return finalString

solution = Solution()
print(solution.reverseVowels("IceCreAm"))