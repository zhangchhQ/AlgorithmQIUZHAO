# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            ret_list.append(root.val)
            dfs(root.right)
        ret_list = []
        dfs(root)
        return ret_list