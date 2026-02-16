import string
class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        alphabet = list(string.ascii_lowercase)
        word_weights = []
        result_word = ""
        for word in words:
            total_weight = 0
            for letter in word:
                total_weight += weights[alphabet.index(letter)]
            word_weights.append(total_weight % 26)
            result_word += alphabet[::-1][total_weight % 26]

        # print(word_weights)
        return result_word

    
print(Solution().mapWordWeights(["abcd","def","xyz"], [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]))
        