"""
输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
"""


import copy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root is None:
            return []
        ret = []
        queue = [root]
        retList = [[root.val]]
        while queue:
            tmpNode = queue.pop(0)
            tmpretList = retList.pop(0)
            if tmpNode.left is None and tmpNode.right is None:
                if sum(tmpretList) == expectNumber:
                    ret.insert(0, tmpretList)
            if tmpNode.left:
                queue.append(tmpNode.left)
                new_tmpretList = copy.copy(tmpretList)
                new_tmpretList.append(tmpNode.left.val)
                retList.append(new_tmpretList)
            if tmpNode.right:
                queue.append(tmpNode.right)
                new_tmpretList = copy.copy(tmpretList)
                new_tmpretList.append(tmpNode.right.val)
                retList.append(new_tmpretList)
        return ret