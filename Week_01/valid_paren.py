class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if not s:
            return True
        if len(s) < 2:
            return False
        for i in s:
            if i == '[':
                stack.append(']')
            elif i == '(':
                stack.append(')')
            elif i == '{':
                stack.append('}')
            else:
                if not stack:
                    return False
                left_last = stack.pop()
                if left_last != i:
                    return False
        return len(stack) == 0
    