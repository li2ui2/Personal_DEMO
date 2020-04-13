"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""


class Solution:
    def jumpFloorII(self, number):
        # write code here
        # 方法1：
        # return pow(2, number-1)
        # 方法2：
        if number < 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        a = 2
        ret = None
        for n in range(2, number):
            ret = a*2
            a = ret
        return ret