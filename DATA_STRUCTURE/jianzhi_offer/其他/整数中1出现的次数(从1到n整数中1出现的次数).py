"""
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
"""


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n <= 0:
            return 0
        total_count = 0
        for value in  range(1, n+1):
            yushu = value % 10
            shang = value // 10
            count = 0
            if yushu == 1:
                count += 1
            if shang == 1:
                    count += 1
            while shang > 9:
                yushu = shang % 10
                if yushu == 1:
                    count += 1
                shang = shang // 10
                if shang == 1:
                    count += 1
            total_count += count
        return total_count
