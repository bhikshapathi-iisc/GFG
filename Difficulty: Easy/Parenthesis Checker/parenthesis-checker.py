class Solution:
    def isBalanced(self, s):
        stack = []
        pair = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            # If opening bracket, push to stack
            if ch in '([{':
                stack.append(ch)
            else:
                # If closing bracket but stack is empty → not balanced
                if not stack:
                    return False
                # Check if it matches top of stack
                if stack[-1] == pair[ch]:
                    stack.pop()
                else:
                    return False

        # Stack should be empty at the end
        return len(stack) == 0
