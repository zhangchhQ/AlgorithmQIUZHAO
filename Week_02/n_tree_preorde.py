"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        run_stack = [root]
        result = []
        temp_root = root
        while run_stack:
            temp_root = run_stack.pop()
            result.append(temp_root.val)
            for child in temp_root.children[::-1]:
                run_stack.append(child)
        return result