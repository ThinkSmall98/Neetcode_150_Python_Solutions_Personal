# Time: O(M(4*3^(L-1))) 
# where M = # of cells in board & L = max len of words
# Space: O(N) where N = total # of letters in dictionary
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True
    
    def pruneWord(self, word) -> None:
        cur = self
        stack = []
        
        for c in word:
            stack.append(cur)
            cur = cur.children[c]
        cur.is_word = False
        
        for t_node, c in reversed(list(zip(stack, word))): # put node & each letter of word together and start at end of word
            if len(t_node.children[c].children) > 0:  # has children
                pass
            else:
                del t_node.children[c]
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        for w in words:
            root.addWord(w)
            
        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()
        
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or 
               (r,c) in visit or board[r][c] not in node.children):
                return
            
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
                node.isWord = False
                root.pruneWord(word)
                
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r,c))
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)
