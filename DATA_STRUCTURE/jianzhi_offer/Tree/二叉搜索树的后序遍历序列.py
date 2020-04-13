"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == []:
            return False

        last = sequence[-1]
        del sequence[-1]
        index = None
        for i in range(len(sequence)):
            if index == None and sequence[i] > last:
                index = i
            if index != None and sequence[i] < last:
                return False
        left_sequence = sequence[:index]
        right_sequence = sequence[index:]
        if left_sequence == []:
            return True
        else:
            left_ret = self.VerifySquenceOfBST(left_sequence)
        if right_sequence == []:
            return True
        else:
            right_ret = self.VerifySquenceOfBST(right_sequence)
        return left_ret and right_ret
