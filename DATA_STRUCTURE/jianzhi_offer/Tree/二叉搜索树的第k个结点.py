"""
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        ret = []
        def mid_order(pRoot):
            if pRoot is None:
                return None
            else:
                mid_order(pRoot.left)
                ret.append(pRoot)
                mid_order(pRoot.right)
        mid_order(pRoot)
        if k <= 0 or k  > len(ret):
            return None
        return ret[k-1]
