"""
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot is None:
            return True
        if pRoot.left is None and pRoot.right is None:
            return True
        result = []
        queue = [(pRoot, [pRoot.val])]
        while queue:
            node, path = queue.pop()
            if node.left is None and node.right is None:
                result.append(path)
            if node.left is not None:
                queue.append((node.left, path + [node.left.val]))
            if node.right is not None:
                queue.append((node.right, path + [node.right.val]))
        ans_max = None
        ans_min = None
        for path in result:
            if ans_max is None:
                ans_max = len(path)
                ans_min = len(path)
            else:
                ans_max = max(ans_max, len(path))
                ans_min = min(ans_min, len(path))
        if len(result) == 1:
            return False
        else:
            if ans_max - ans_min <= 1:
                return True
            else:
                return False
