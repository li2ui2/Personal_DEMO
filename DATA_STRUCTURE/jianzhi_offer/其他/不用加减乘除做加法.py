class Solution:
    def Add(self, num1, num2):
        # write code here
        xorNum = num1 ^ num2
        andNum = (num1 & num2) << 1
        while andNum != 0:
            temp1 = (xorNum ^ andNum) & 0xFFFFFFFF
            temp2 = ((xorNum & andNum) << 1) & 0xFFFFFFFF
            xorNum = temp1
            andNum = temp2
        # 一个负整数（或原码）与其补数（或补码）相加，和为模
        # return xorNum if xorNum <= 0x7FFFFFFF else xorNum - 0x100000000
        return xorNum if xorNum <= 0x7FFFFFFF else ~(xorNum ^ 0xffffffff)
