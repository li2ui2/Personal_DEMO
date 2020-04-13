class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        a = 2
        b = 1
        ret = None
        for n in range(2, number):
            ret = a + b
            b = a
            a = ret
        return ret