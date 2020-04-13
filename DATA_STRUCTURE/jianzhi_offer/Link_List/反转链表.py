"""
输入一个链表，反转链表后，输出新链表的表头。
"""

class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        last = None
        while pHead:
            cur = pHead.next
            pHead.next = last
            last = pHead
            pHead = cur
        return last
