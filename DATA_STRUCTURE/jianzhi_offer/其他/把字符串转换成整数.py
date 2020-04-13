"""
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。
数值为0或者字符串不是一个合法的数值则返回0
"""


def StrToInt(s):
    # write code here
    n = len(s)
    if n == 0:
        return 0
    else:
        ans = None
        if s[0] > "9" or s[0] < "0":
            ans = 0
        else:
            ans = int(s[0]) * 10 ** (n - 1)
        for i in range(1, n):
            if s[i] > "9" or s[i] < "0":
                return 0
            else:
                ans += int(s[i]) * 10 ** (n - i - 1)
        if s[0] == "+":
            return ans
        if s[0] == "-":
            return -ans
        return ans


if __name__ == '__main__':
    print(StrToInt("+19209"))
