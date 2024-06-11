class Solution:
    # Time: O(n)
    # Space: O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # index, temperature
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stack_i, _  = stack.pop()
                res[stack_i] = i - stack_i
            stack.append((i, temp))
        return res

'''
1. Keep stack of tuple (index, temperature)
2. Go through each temperature in temperatures arr and 
    if the value of the stack is less than the current temp pop from stack
    and subtract current day by the day of the stack.
3. Then outside of while loop append the tuple to stack
'''
