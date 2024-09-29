class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        vc = {vowel: 0 for vowel in vowels} # vowels count
        kc = 0 # constonants count
        lp = 0
        rp = 0
        sc = 0 # substring count

        while rp != len(word):
            # print(f'lp / rp: {lp}/{rp}')
            # print(f'vowel counts: {vc}')
            # print(f'consonants count: {kc}')

            if kc > k:
                if word[lp] in vc:
                    vc[word[lp]] -= 1
                else:
                    kc -= 1
                lp += 1
            elif 0 in vc.values():
                if word[rp] in vc:
                    vc[word[rp]] += 1
                else:
                    kc += 1
                rp += 1
            # if there arent enough vowels, increase rp
            elif kc < k:
                if word[rp] in vc:
                    vc[word[rp]] += 1
                else:
                    kc += 1
                rp += 1
            elif kc == k:
                # print(f'substring that is valid: {word[lp:rp]}')
                sc += 1
                if rp > lp:
                    if word[rp] in vc:
                        vc[word[rp]] += 1
                    else:
                        kc += 1
                    rp += 1
                else:
                    if word[lp] in vc:
                        vc[word[lp]] -= 1
                    else:
                        kc -= 1
                    lp += 1

            if rp == len(word):
                    if kc == k and 0 not in vc.values():
                        sc +=1
            # print()

        while lp != len(word)-1:
            if word[lp] in vc:
                vc[word[lp]] -= 1
            else:
                kc -= 1
            lp += 1
            if kc == k and 0 not in vc.values():
                sc += 1
        return sc

print(Solution().countOfSubstrings('ieiaoud', 0)) # ieiaou and eiaou
# print(Solution().countOfSubstrings('ieaouqqieaouqq', 1))
# print(Solution().countOfSubstrings('aeiou', 0))
# print(Solution().countOfSubstrings('aeioqq', 1))
# print(Solution().countOfSubstrings('aeiouqq', 1))
# print(Solution().countOfSubstrings('aeiouqq', 2))

            