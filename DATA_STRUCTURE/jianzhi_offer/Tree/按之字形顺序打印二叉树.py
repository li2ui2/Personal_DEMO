"""
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Print(self, pRoot):
        if pRoot is None:
            return []

        stack1 = [pRoot]
        stack2 = []
        ret = []
        while stack1 or stack2:
            if stack1:
                ret1 = []
                while stack1:
                    tempNode = stack1.pop()
                    ret1.append(tempNode.val)
                    if tempNode.left:
                        stack2.append(tempNode.left)
                    if tempNode.right:
                        stack2.append(tempNode.right)
                ret.append(ret1)
            if stack2:
                ret2 = []
                while stack2:
                    tempNode = stack2.pop()
                    ret2.append(tempNode.val)
                    if tempNode.right:
                        stack1.append(tempNode.right)
                    if tempNode.left:
                        stack1.append(tempNode.left)
                ret.append(ret2)
        return ret