"""
请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        def isTrue(leftNode, rightNode):
            if leftNode is None and rightNode is None:
                return True
            if leftNode is None or rightNode is None:
                return False
            if leftNode.val != rightNode.val:
                return False
            ret1 = isTrue(leftNode.left, rightNode.right)
            ret2 = isTrue(leftNode.right, rightNode.left)
            return ret1 and ret2

        if pRoot is None:
            return True
        else:
            return isTrue(pRoot.left, pRoot.right)