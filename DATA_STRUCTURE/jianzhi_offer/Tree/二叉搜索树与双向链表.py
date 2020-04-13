"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree is None:
            return None
        leftNode = self.Convert(pRootOfTree.left)
        rightNode = self.Convert(pRootOfTree.right)

        def find(leftNode):
            while leftNode.right:
                leftNode = leftNode.right
            return leftNode

        ret = leftNode
        if leftNode:
            leftNode = find(leftNode)
        else:
            ret = pRootOfTree

        pRootOfTree.left = leftNode
        if leftNode is not None:
            leftNode.right = pRootOfTree
        pRootOfTree.right = rightNode
        if rightNode is not None:
            rightNode.left = pRootOfTree
        return ret