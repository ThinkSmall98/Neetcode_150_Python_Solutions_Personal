class Solution:
  # Time: O(n)
  # Space: O(n)
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = [] # time
        for p, s in sorted(pair)[::-1]: # sort the positions & go from right to left
            stack.append((target - p)/ s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
'''
1. Zip positions & speed into it's own list
2. Keep a stack of time
3. Sort position from biggest to smallest.
4. Iterate thru each pair and append times to stack
5. Pop from stack if the last value <= 2nd to last value
6. Return len of stack
'''
