class Solution(object):
    def isValid(self, s):
        stack = []
        map_char = {")":"(", "}":"{", "]":"["}
        for char in s:
            # if char is closing bracket
            if char in map_char:
                if stack:
                    top_element = stack.pop() 
                    if map_char[char] != top_element:
                        return False
                else:
                    return False # found closed bracket before any open ones
                
            # if char is opening bracket
            else:
                stack.append(char)
        # True if stack is empty, False is stack isn't empty ((()
        return not stack
'''
Open/closed Parantheses must be next to each other
1. Start with dict mapping closed to open parentheses
2. Create stack to keep track of open parentheses
3. Go thru each char, find last element by popping if stack not empty else return False immediately
4. if char not in dict keys, append to stack bc it's open bracket
5. return True if stack empty else False
'''
