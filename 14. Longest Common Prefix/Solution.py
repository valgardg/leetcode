class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        trie = Trie()
        for word in strs:
            if word == "":
                return ""
            trie.insert(word)
        node = trie.root
        longest_common_prefix = ""
        while len(node.children.keys()) == 1 and len(longest_common_prefix) < min([len(word) for word in strs]):
            longest_common_prefix += list(node.children.keys())[0]
            node = node.children[list(node.children.keys())[0]]

        return longest_common_prefix
