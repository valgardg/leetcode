class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        r = {} # required
        e = {} # existing
        for char in word2:
            if char in r:
                r[char] += 1
            else:
                r[char] = 1

        for char in word1:
            if char in e:
                e[char] += 1
            else:
                e[char] = 1

        if sorted(r.values()) == sorted(e.values()) and sorted(r.keys()) == sorted(e.keys()):
            return True

        return False
    
print(Solution().closeStrings('abc', 'bca'))
print(Solution().closeStrings('a', 'aa'))
print(Solution().closeStrings('cabbba', 'abbccc'))
# print(Solution().closeStrings('abc', 'bca'))