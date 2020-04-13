"""
leetcode 438
给定一个字符串 s 和一个非空字符串 p，
找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
输入:
s: "cbaebabacd" p: "abc"
输出:
[0, 6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
"""


import collections


def findAnagrams(s, p):
    pLen = len(p)
    sLen = len(s)
    if sLen < pLen or s == [] or p == []:
        return []
    count = collections.Counter(p)
    left = 0
    result = []
    tempLen = 0
    for right in range(sLen):
        count[s[right]] -= 1
        if count[s[right]] >= 0:
            tempLen += 1
        if right >= pLen:
            count[s[left]] += 1
            if count[s[left]] >= 1:
                tempLen -= 1
            left += 1
        if pLen == tempLen:
            result.append(left)
    return result


if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    print(findAnagrams(s, p))
