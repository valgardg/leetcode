from typing import List
class Solution:
    # returns true if the substring given can be rearranged to have a prefix equal to match
    def canRearrange(self, substring, match):
        subs = list(substring)
        for char in list(match):
            if char in subs:
                subs.remove(char)
            else:
                return False
            
        return True

    def validSubstringCount(self, word1: str, word2: str) -> int:
        count = 0
        for x in range(len(word1)):
            for i in range(x+1, len(word1)+1):
                # print(i)
                substring = word1[x:i]
                if(len(substring) < len(word2)):
                    pass
                else:
                    if self.canRearrange(substring,word2):
                        count +=1
        
        return count

# print(Solution().canRearrange("aabc", "abd"))

# print(Solution().validSubstringCount("bcca", "abc"))
print(Solution().validSubstringCount("abcabc", "abc"))


# were given
# bcca
# we want to check 
# bcc  
# bcca