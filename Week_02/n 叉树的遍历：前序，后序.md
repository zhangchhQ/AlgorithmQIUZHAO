#### n 叉树的遍历：前序，后序

![微信图片_20200722105211](E:\leetcode\AlgorithmQIUZHAO\Week_02\图\微信图片_20200722105211.png)

##### 如何理解孩子节点

​	1的孩子节点是[3， 2， 4]，3的孩子节点时[5， 6]

##### 代码过程 

​	维护一个栈存放节点，先进后出，用来维护遍历顺序

​	一个结果栈保留结果

前序遍历：

```python
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
            # 每个孩子节点反着进 3后进先出 5后进先出
            for child in temp_root.children[::-1]:
                run_stack.append(child)
        return result
```

后序遍历：

```python
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
            temp_root = run_stack.pop()
			result.append(temp_root.val)
            for child in temp_root.children:
                run_stack.append(child)
        # 孩子节点按顺序入栈，但由于栈先进后出，result的结果是反的
        return result[::-1]
```

```
# 递归法
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(root):
            if not root:
                return
            for node in root.children:
            # 会递归到最底层节点，再返回来，从底向上从左至右进行遍历，若childern[::-1]表示从右至左
                dfs(node)
            ret_list.append(root.val)
        ret_list = []
        dfs(root)
        return ret_list
```

