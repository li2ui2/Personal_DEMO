"""
leetcode 76 hard
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
"""
import collections


class Solution:
    def minWindow(self, s, t):
        if len(s) < len(t):
            return ""
        str_count = collections.Counter(t)
        left = 0
        count = len(t)
        maxLength = len(s) + 1
        result = ""
        for right in range(len(s)):
            str_count[s[right]] -= 1
            if str_count[s[right]] >= 0:
                count -= 1
            while left < right and str_count[s[left]] < 0:
                str_count[s[left]] += 1
                left += 1
            if count == 0 and maxLength > right - left + 1:
                maxLength = right - left + 1
                result = s[left: right+1]
        return result


if __name__ == '__main__':
    S = "ADOBECODEBANC"
    T = "ABC"
    s = Solution()
    print(s.minWindow(S, T))
