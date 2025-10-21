# 211. Design Add and Search Words Data Structure

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
