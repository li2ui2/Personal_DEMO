"""
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法。
"""


class Solution:
    def __init__(self):
        self.stack = []
        self.minlist = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.minlist == []:
            self.minlist.append(node)
        else:
            if self.minlist[-1] > node:
                self.minlist.append(node)
            else:
                self.minlist.append(self.minlist[-1])

    def pop(self):
        # write code here
        if self.stack == []:
            return None
        else:
            self.minlist.pop()
            return self.stack.pop()

    def top(self):
        # write code here
        if self.stack == []:
            return None
        else:
            return self.stack[-1]

    def min(self):
        # write code here
        if self.minlist == []:
            return None
        else:
            return self.minlist[-1]