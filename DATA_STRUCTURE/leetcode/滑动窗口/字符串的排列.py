"""
leetcode 576
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
"""


import collections


class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        s_dict = collections.Counter(s1)

        left = 0
        tempLen = 0
        s1Len = len(s1)
        result = False
        for right in range(len(s2)):
            s_dict[s2[right]] -= 1
            if s_dict[s2[right]] >= 0:
                tempLen += 1
            if right >= s1Len:
                s_dict[s2[left]] += 1
                if s_dict[s2[left]] >= 1:
                    tempLen -= 1
                left += 1
            if tempLen == s1Len:
                return True
        return result