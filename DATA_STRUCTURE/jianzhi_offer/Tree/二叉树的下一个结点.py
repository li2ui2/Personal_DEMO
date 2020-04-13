"""
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

        
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode is None:
            return None
        if pNode.right:
            retNode = pNode.right
            while retNode.left:
                retNode = retNode.left
            return retNode
        else:
            retNode = pNode
            while retNode.next:
                if retNode.next.left == retNode:
                    return retNode.next
                retNode = retNode.next
            return None
