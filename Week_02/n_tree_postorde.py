"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        run_stack = [root]
        result = []
        while run_stack:
            temp = run_stack.pop()
            result.append(temp.val)
            for child in temp.children:
                run_stack.append(child)
        return result[::-1]