"""
利用字符重复出现的次数，编写一个方法，实现基本的字符串压缩功能。
比如，字符串“aabcccccaaa”经压缩会变成“a2b1c5a3”。
若压缩后的字符串没有变短，则返回原先的字符串。
给定一个string iniString为待压缩的串(长度小于等于10000)，
保证串内字符均由大小写英文字母组成，返回一个string，为所求的压缩后或未变化的串。

测试样例
"aabcccccaaa"
返回："a2b1c5a3"
"welcometonowcoderrrrr"
返回："welcometonowcoderrrrr"
"""


class Zipper:
    # def zipString(self, iniString):
    #     zipStr = ""
    #     strCnt = 1
    #     for i in range(len(iniString) - 1):
    #         if iniString[i + 1] == iniString[i]:
    #             strCnt += 1
    #         else:
    #             zipStr += iniString[i] + str(strCnt)
    #             strCnt = 1
    #     zipStr += iniString[-1] + str(strCnt)
    #     return zipStr if len(zipStr) < len(iniString) else iniString

    def zipString(self, iniString):
        # write code here
        ans = ""
        n = len(iniString)
        temp = 1
        pos = 1
        for i in range(1, n):
            if iniString[i] == iniString[i - 1]:
                temp += 1
                pos += 1
            else:
                temp = 1
            if temp == 1:
                ans = ans + iniString[i-1] + str(pos)
                pos = 1
        ans = ans + iniString[-1] + str(pos)
        ansLen = len(ans)
        if ansLen >= n:
            return iniString
        return ans


if __name__ == '__main__':
    s = Zipper()
    iniString = "aabcccccaaa"
    print(s.zipString(iniString))
