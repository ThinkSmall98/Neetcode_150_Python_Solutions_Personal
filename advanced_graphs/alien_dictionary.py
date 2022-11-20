# Time complexity : O(C). Building the adjacency list has a time complexity of O(C)
# C = total length of all the words in the input list, added together
# U = total number of unique letters in the alien alphabet. 
# While this is limited to 26, we'll still look if it was not limited
# N = total number of strings in input list
# Space complexity : O(1) or O(U+min⁡(U^2,N))
# Num of edges in the worst case is min⁡(U^2,N)
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j]) # chars next to each other lexicographically
                    break
        visited = {} # {char: bool}. False= visited. True= current path
        res = []
        def dfs(char):
            if char in visited: # check whether it's true or false. If true, there's a cycle
                return visited[char]
            visited[char] = True
            for neiChar in adj[char]:
                if dfs(neiChar):
                    return True
            visited[char] = False
            res.append(char)
        for char in adj:
            if dfs(char):
                return ""
        res.reverse()
        return "".join(res)
