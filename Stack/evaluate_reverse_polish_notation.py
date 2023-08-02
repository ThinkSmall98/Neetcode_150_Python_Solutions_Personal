class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == '+':
                stack.append(stack.pop() + stack.pop())
            elif char == '-':    
                stack.append((stack.pop() - stack.pop()) * -1)
            elif char == '*':  
                stack.append(stack.pop() * stack.pop())
            elif char == '/': 
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second/first)) # can't get rid of first & second otherwise edge case where we divide by 0
            else:
                stack.append(int(char))     
        return stack[0]

# In reverse Polish notation, operators follow their operands
# Use int() instead of floor
