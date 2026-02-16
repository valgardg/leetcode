class Solution(object):
    def prefixConnected(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: int
        """

        prefixes = dict()
        for word in words:
            if len(word) < k:
                continue
            if word[:k] not in prefixes:
                prefixes[word[:k]] = 1
            else:
                prefixes[word[:k]] += 1
        
        return len([x for x in prefixes.values() if x > 1])
        

print(Solution().prefixConnected(["bat","dog","dog","doggy","bat"], 3))