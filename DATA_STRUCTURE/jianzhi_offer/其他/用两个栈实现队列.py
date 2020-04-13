"""
用两个栈来实现一个队列，完成队列的Push和Pop操作。
队列中的元素为int类型。
"""


class Solution:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, node):
        # write code here
        self.stack_in.append(node)

    def pop(self):
        # return xx
        if self.stack_out == []:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()
