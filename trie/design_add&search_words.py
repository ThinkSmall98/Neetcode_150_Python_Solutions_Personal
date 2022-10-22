class TrieNode:
    def __init__(self):
        self.children = {}  # a : TrieNode
        self.word = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        self.max_word_len = 0

    # Time: O(m), Space: O(m) where m = key len
    def addWord(self, word: str) -> None:
        cur = self.root
        self.max_word_len = max(self.max_word_len, len(word))
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    #Time: O(m) for words w/o dots, O(n * 26^m) for words with dots, Space: O(n) where n = # of keys, m = key len
    def search(self, word: str) -> bool:
        if len(word) > self.max_word_len:
            return False
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
