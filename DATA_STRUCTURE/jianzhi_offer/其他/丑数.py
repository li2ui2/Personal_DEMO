"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        # 设置3个丑数指针，two，three,five
        if index == 0:
            return 0
        two = 0
        three = 0
        five = 0
        uglyList = [1]
        count = 1
        while count != index:
            minValue = min(2*uglyList[two], 3*uglyList[three], 5*uglyList[five])
            uglyList.append(minValue)
            count += 1
            if minValue == 2*uglyList[two]:
                two += 1
            if minValue == 3*uglyList[three]:
                three += 1
            if minValue == 5*uglyList[five]:
                five += 1
        return uglyList[count-1]
