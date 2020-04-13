"""
leetcode 3
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""
import collections


def lengthOfLongestSubstring(s):
    n = len(s)
    if s is None or n == 0:
        return 0
    count = collections.Counter()
    left = 0
    result = 1
    for right in range(n):
        count[s[right]] += 1
        while count[s[right]] != 1:
            count[s[left]] -= 1
            left += 1
        result = max(result, right - left + 1)
    return result


if __name__ == '__main__':
    s = "pwwkew"
    print(lengthOfLongestSubstring(s))
