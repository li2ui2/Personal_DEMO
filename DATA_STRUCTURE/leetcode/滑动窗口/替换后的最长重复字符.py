"""
leetcode 424
给你一个仅由大写英文字母组成的字符串，
你可以将任意位置上的字符替换成另外的字符，
总共可最多替换 k 次。在执行上述操作后，
找到包含重复字母的最长子串的长度。
输入:
s = "ABAB", k = 2

输出:
4
"""
import collections


class Solution:
    def characterReplacement(self, s, k):
        if len(s) == 0 or s is None:
            return 0
        count = collections.Counter()
        left = 0
        result = 0
        cur_max = 0  # 记录最长重复字母个数
        for right in range(len(s)):
            count[s[right]] += 1
            cur_max = max(cur_max, count[s[right]])
            while right - left + 1 - cur_max > k:
                count[s[left]] -= 1
                left += 1
            result = max(right - left + 1, result)
        return result


if __name__ == '__main__':
    s = Solution()
    A = "ABAB"
    k = 2
    print(s.characterReplacement(A, k))
