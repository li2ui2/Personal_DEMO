"""
统计一个数字在排序数组中出现的次数。
"""


import collections


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        count = collections.Counter(data)
        return count[k]
