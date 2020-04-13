"""
输入两个单调递增的链表，输出两个链表合成后的链表，
当然我们需要合成后的链表满足单调不减规则。
"""

class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        newHead = pHead1 if pHead1.val < pHead2.val else pHead2
        tmp1 = pHead1
        tmp2 = pHead2
        previousPointer = newHead
        if newHead == tmp1:
            tmp1 = tmp1.next
        else:
            tmp2 = tmp2.next
        while tmp1 and tmp2:
            if tmp1.val < tmp2.val:
                previousPointer.next = tmp1
                previousPointer = tmp1
                tmp1 = tmp1.next
            else:
                previousPointer.next = tmp2
                previousPointer = tmp2
                tmp2 = tmp2.next
        if tmp1 == None:
            previousPointer.next = tmp2
        else:
            previousPointer.next = tmp1
        return newHead