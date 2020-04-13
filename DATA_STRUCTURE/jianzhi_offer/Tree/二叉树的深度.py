"""
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if pRoot is None:
            return 0
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
        ans = None
        for path in result:
            if ans is None:
                ans = len(path)
            else:
                ans = max(ans, len(path))
        return ans