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


def print_trie_tree(node, level=0):
    for char, child in node.children.items():
        print("  " * level + f"- {char}" + (" *" if child.is_end else ""))
        print_trie_tree(child, level + 1)
