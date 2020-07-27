"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return
        out = []
        queue = [root]
        while queue:
            child = []
            node = []
            # for item in queue:                                  #因为是N叉树,所以需要遍历
            #     child.append(item.val)
            #     if item.children: node += item.children

            for item in queue:
                if item.children:
                    # 保证列表中没有别的列表，append会造成列表套列表，导致后续的item是列表而不是root
                    node += item.children
                    # node.append(item.children)
                child.append(item.val)
            out.append(child)
            # child 存有每一层元素的信息 queue=child：准备下一层遍历的元素
            queue = node
        return out