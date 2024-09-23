class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        lp = 0
        rp = 0
        mc = 0

        vowel_count = 0
        max_count = 0

        vowels = ['a','e','i','o','u']
        while rp < len(s):

            if s[rp] in vowels:
                vowel_count += 1

            rp += 1
            if(rp - lp > k):
                if s[lp] in vowels:
                    vowel_count -=1
                lp += 1
            if vowel_count > max_count:
                max_count = vowel_count

        return max_count
    
# print(Solution().maxVowels("abcdiiidef", k=3))
# print(Solution().maxVowels("aeiou", k=2))
# print(Solution().maxVowels("leetcode", k=3))
print(Solution().maxVowels("weallloveyou", k=7))