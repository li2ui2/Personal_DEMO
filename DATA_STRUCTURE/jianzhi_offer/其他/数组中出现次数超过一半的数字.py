"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        """
        di = {}
        for i in numbers:
            di[i] = di.get(i,0) + 1
        for key in di.keys():
            # print(di[key])
            if di[key] > len(numbers)/2.0:
                return key
        return 0
        """
        # 思路：遇到不相同的数据就相互抵消掉，最终剩下的数据就可能是大于一般的数字
        last = 0
        lastCount = 0
        for num in numbers:
            if lastCount == 0:
                last = num
                lastCount = 1
            else:
                if num == last:
                    lastCount += 1
                else:
                    lastCount -= 1
        if lastCount == 0:
            return 0
        else:
            # 这种情况下，last可能是大于一半的数字
            lastCount = 0
            for num in numbers:
                if num == last:
                    lastCount += 1
                if lastCount > (len(numbers)>>1):
                    return last
        return 0
