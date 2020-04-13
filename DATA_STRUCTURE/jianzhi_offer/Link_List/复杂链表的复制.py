"""
输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""


import copy


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

        
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        # return copy.deepcopy(pHead)
        if not pHead:
            return None
        # 复制一个一样的node，并且添加到之前的链表的每一个node后面
        ptmp = pHead
        while ptmp:
            node = RandomListNode(ptmp.label)
            node.next = ptmp.next
            ptmp.next = node
            ptmp = node.next
        # 实现新建的node的random的指向
        ptmp = pHead
        while ptmp:
            if ptmp.random:
                ptmp.next.random = ptmp.random.next
            ptmp = ptmp.next.next
        # 断开原来的node和新的node之间的链接
        ptmp = pHead
        newHead = pHead.next
        pNewtmp = newHead
        while ptmp:
            ptmp.next = ptmp.next.next
            if pNewtmp.next:
                pNewtmp.next = pNewtmp.next.next
                pNewtmp = pNewtmp.next
            ptmp = ptmp.next
        return newHead