"""
输入两个链表，找出它们的第一个公共结点。
（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）
"""


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        ptmp1 = pHead1
        ptmp2 = pHead2
        while ptmp1 and ptmp2:
            if ptmp1 == ptmp2:
                return ptmp1
            ptmp1 = ptmp1.next
            ptmp2 = ptmp2.next
        if ptmp1:
            k = 0
            while ptmp1:
                ptmp1 = ptmp1.next
                k += 1
            ptmp1 = pHead1
            ptmp2 = pHead2
            for i in range(k):
                ptmp1 = ptmp1.next
            while ptmp1 != ptmp2:
                ptmp1 = ptmp1.next
                ptmp2 = ptmp2.next
            return ptmp1
        if ptmp2:
            k = 0
            while ptmp2:
                ptmp2 = ptmp2.next
                k += 1
            ptmp1 = pHead1
            ptmp2 = pHead2
            for i in range(k):
                ptmp2 = ptmp2.next
            while ptmp1 != ptmp2:
                ptmp1 = ptmp1.next
                ptmp2 = ptmp2.next
            return ptmp2