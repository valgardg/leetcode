from typing import List
class Solution:
    def initMpp(self, word2):
        mpp = {}
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        for char in alphabet:
            mpp[char] = [0,0]

        for char in word2:
            mpp[char][1] += 1
        return mpp
        
    def validSubstringCount(self, word1: str, word2: str) -> int:
        # initialize variables
        count = 0
        mpp = self.initMpp(word2)
        lp = 0
        rp = 0
        n = len(word1)
        m = len(word2)
        size = 0

        # continue until our right pointer reaches end of string as we want to capture all possible substrings
        while rp < n:
            while size == m and lp <= rp:
                count += (n - rp + 1)
                # when we move lp to the right, the current pointed character is no longer in our sliding window
                mpp[word1[lp]][0] -= 1
                # if the number of word1[lp] characters in word2 is not zero and we dont have as many of them we reduce size
                if mpp[word1[lp]][1] > 0 and mpp[word1[lp]][0] < mpp[word1[lp]][1]:
                    size -= 1
                lp += 1
            
            # if the current character word1[rp] is in word2 and we havent found enough for word2, increment size and count
            if mpp[word1[rp]][1] > 0 and mpp[word1[rp]][0] < mpp[word1[rp]][1]:
                size += 1
            mpp[word1[rp]][0] += 1
            
            # move right pointer forward
            rp += 1

        # once our right pointer reaches end of string, we finish off moving left pointer over to the right
        while size == m and lp <= rp:
            count += (n - rp + 1)
            mpp[word1[lp]][0] -= 1
            if mpp[word1[lp]][1] > 0 and mpp[word1[lp]][0] < mpp[word1[lp]][1]:
                    size -= 1
            lp += 1

        return count

print(Solution().validSubstringCount("abcabc", "abc"))