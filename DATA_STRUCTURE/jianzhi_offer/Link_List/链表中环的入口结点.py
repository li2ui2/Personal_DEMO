"""
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
"""


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        # 方法1：利用python中的集合来做
        """
        if pHead == None:
            return None
        res = set()
        n = len(res)
        while pHead:
            res.add(pHead)
            if n == len(res):
                return pHead
            pHead = pHead.next
            n = len(res)
        return None
        """
        # 方法二：设置快慢指针
        if pHead == None:
            return None
        fast = pHead
        slow = pHead
        # 判断是否有环，若快慢指针相遇，则说明有环；若最终fast为None，则说明无环
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break

        if fast is None or fast.next is None:
            return None

        # 快慢指针相遇后，慢指针再走m步，即从pHead首节点到入口节点的距离
        temp = pHead
        while temp != slow:
            temp = temp.next
            slow = slow.next
        return slow