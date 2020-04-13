"""
输入一个链表，输出该链表中倒数第k个结点。
"""

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        temp = []
        while head != None:
            temp.append(head)
            head = head.next
        if k>len(temp) or k<1:
            return
        return temp[-k]
