class Solution(object):
    def isValid(self, s):
        stack = []
        map_char = {")":"(", "}":"{", "]":"["}
        for char in s:
            # if char is closing bracket
            if char in map_char:
                if stack:
                    top_element = stack.pop() 
                else:
                    top_element = "0" # dummy value
                if map_char[char] != top_element:
                    return False
            # if char is opening bracket
            else:
                stack.append(char)
        # True if stack is empty, False is stack isn't empty ((()
        return not stack
