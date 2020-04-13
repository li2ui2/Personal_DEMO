"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""


class Solution:
    def NumberOf1(self, n):
        # write code here

        count = 0
        while n != 0:
            count += 1
            n = n & (n - 1)
            n = 0xffffffff & n
        return count

        # count = 0
        # n = 0xffffffff & n
        # for i in str(bin(n)):
        #     if i == "1":
        #         count += 1
        # return count
