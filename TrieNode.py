# 211. Design Add and Search Words Data Structure

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
