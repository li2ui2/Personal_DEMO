"""
leetcode 992
给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，
则称 A 的这个连续、不一定独立的子数组为好子数组。
输入：A = [1,2,1,2,3], K = 2
输出：7
解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
"""


import collections


class Solution:
    def subarraysWithKDistinct(self, A, K):
        if len(A) == 0 or K <=0:
            return 0
        # 滑动窗口求解
        count = collections.Counter()
        left = 0
        results = 0
        result = 1
        temp = 0
        for right in range(len(A)):
            count[A[right]] += 1
            if count[A[right]] == 1:
                temp += 1
            while count[A[left]] > 1 or temp > K:
                if temp > K:
                    result = 1
                    temp -= 1
                else:
                    result += 1
                count[A[left]] -= 1
                left += 1
            if temp == K:
                results += result
        return results


if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 1, 2, 3]
    K = 2
    print(s.subarraysWithKDistinct(A, K))
