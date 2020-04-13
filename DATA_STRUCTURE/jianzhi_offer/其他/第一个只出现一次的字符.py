"""
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
"""
import collections


class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s) == 0:
            return -1
        count = collections.Counter(s)
        temp = []
        for key in count:
            if count[key] == 1:
                temp.append(s.index(key))
        if temp:
            return min(temp)
        else:
            return -1