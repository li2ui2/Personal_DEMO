"""
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

保证base和exponent不同时为0
"""


class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent == 0:
            return 1
        ret = base
        if exponent > 0:
            for i in range(1, exponent):
                ret *= base
            return ret
        else:
            for i in range(1, abs(exponent)):
                ret *= base
            return 1/ret