# Time Complexity: O(∣E∣^d) where ∣E∣ = num of total flights and d = maximum number of flights from an airport.
# This is total # of combinations possible. Sampling with replacement & order matters. Sample of size k with population of size n.
# Space Complexity: O(∣V∣+∣E∣) where ∣V∣= # of airports & ∣E∣ = num of total flights

# In the algorithm, we use the graph as well as the visit bitmap, which would require the space of ∣V∣+∣E∣.

# Since we applied recursion in the algorithm, which would incur additional memory consumption in the function call stack. The maximum depth of the recursion would be exactly the number of flights in the input, i.e.∣E∣.

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort() # lexigraphical order
        adj = {src: [] for src, _ in tickets}
        for src, dest in tickets:
            adj[src].append(dest)
        res = ['JFK']
        def dfs(src):
            if len(tickets) + 1 == len(res):
                return True
            if src not in adj:
                return False
            temp = adj[src]
            for i, dest in enumerate(temp):
                adj[src].pop(i)
                res.append(dest)

                if dfs(dest): return True

                # backtrack
                adj[src].insert(i, dest)
                res.pop()
            return False
        dfs('JFK')
        return res





