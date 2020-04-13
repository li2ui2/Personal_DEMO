"""
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
"""


def isNumeric(s):
    # write code here
    if not s:
        return False
    Length = len(s)
    while s[0] == " ":
        s = s[1:]
    # 判断第一个字符是否为数字和正负号
    if s[0] not in "+-" and not s[0].isdigit():
        return False
    # 判断字符串中是否包含"."
    if "." in s[1:]:
        # 判断"e"和"E"是不是在"."之后
        if "e" in s[1:]:
            if s.index("e") < s.index("."):
                return False
        # 判断是否出现了多个"."
        temp = s.split(".")
        if len(temp) != 2:
            return False
        else:
            # 若只有一个"."，那么，将"."的前后两部分进行递归判断
            for i in temp:
                if not self.isNumeric(i):
                    return False
            return True
    # 接着从s的第二个字符开始判断
    for i in range(1, Length):
        # 若s[i]为非数字的情况
        if not s[i].isdigit():
            # 若为"e"或者"E"
            if s[i] == "e" or s[i] == "E":
                # 若s[i]为"e"或者"E"，且出现在字符串末尾
                if i == Length - 1:
                    return False
                # 若s[i]为"e"或者"E"，且后一个字符不是数字和正负号的话
                if s[i + 1] != "-" and not s[i + 1].isdigit() and s[i + 1] != "+":
                    return False
                continue
            # 若s[i]为"-"或者"+"
            if s[i] == "-" or s[i] == "+":
                # 若s[i - 1]不为"e"或者"E"
                if s[i - 1] is not "e" and s[i - 1] is not "E":
                    return False
                continue
            if s[i] == " ":
                continue
            return False
    return True
