# Time Complexity: O(M^2*N), where M = len of each word & N = len(wordList)
# Space Complexity: O(M^2*N)
from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        neighbors = defaultdict(list)
        # Generate adjacency list
        for word in wordList:
            for j in range(len(word)):
                # use '*' as wildcard placeholder
                pattern = word[:j] + "*" + word[j+1:]
                neighbors[pattern].append(word)
        # shortest path = BFS
        visited = set()
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for pattern_word in neighbors[pattern]:
                        if pattern_word not in visited:
                            visited.add(pattern_word)
                            q.append(pattern_word)
            res += 1
        return 0

