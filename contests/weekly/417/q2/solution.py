class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        vc = {vowel: 0 for vowel in vowels} # vowels count
        kc = 0 # constonants count
        lp = 0
        rp = 0
        sc = 0 # substring count

        

print(Solution().countOfSubstrings('iqeaouqi', 2)) # correct answer is 3
# print(Solution().countOfSubstrings('ieiaoud', 0)) # ieiaou and eiaou
# print(Solution().countOfSubstrings('ieaouqqieaouqq', 1))
# print(Solution().countOfSubstrings('aeiou', 0))
# print(Solution().countOfSubstrings('aeioqq', 1))
# print(Solution().countOfSubstrings('aeiouqq', 1))
# print(Solution().countOfSubstrings('aeiouqq', 2))

            