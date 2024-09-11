class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in bracket_map:
                top_elt = stack.pop() if stack else '#'
                if bracket_map[char] != top_elt:
                    return False
            else:
                stack.append(char)
        # If stack not empty, all brackets are properly closed
        return not stack