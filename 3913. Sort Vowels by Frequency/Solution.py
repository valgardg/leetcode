class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiou"
        freqs = {}

        for i, c in enumerate(s):
            if c in vowels:
                if c in freqs:
                    freqs[c][1] += 1
                else:
                    freqs[c] = [len(s) - i, 1]
        
        finals = ""
        vowelstack = []
        print(freqs)
        for k, f in dict(sorted(freqs.items(), key=lambda item: (item[1][1], item[1][0]), reverse=True)).items():
            for i in range(f[1]):
                vowelstack.append(k)
        print(vowelstack)
        for c in s:
            if c in vowels:
                finals += vowelstack.pop(0)
            else:
                finals += c
        
        return finals
    

# print(Solution().sortVowels("leetcode"))
print(Solution().sortVowels("baeiou"))
print(Solution().sortVowels("aeiaaioooa"))
