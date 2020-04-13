"""
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        queue1 = [pRoot]
        queue2 = []
        ret = []
        while queue1 or queue2:
            if queue1:
                ret1 = []
                while queue1:
                    tempNode = queue1.pop(0)
                    ret1.append(tempNode.val)
                    if tempNode.left:
                        queue2.append(tempNode.left)
                    if tempNode.right:
                        queue2.append(tempNode.right)
                ret.append(ret1)
            if queue2:
                ret2 = []
                while queue2:
                    tempNode = queue2.pop(0)
                    ret2.append(tempNode.val)
                    if tempNode.left:
                        queue1.append(tempNode.left)
                    if tempNode.right:
                        queue1.append(tempNode.right)
                ret.append(ret2)
        return ret