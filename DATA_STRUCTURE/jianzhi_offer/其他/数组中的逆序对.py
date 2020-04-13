"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。
并将P对1000000007取模的结果输出。 即输出P%1000000007
"""
# 以下解法O(nlogn)
count = 0


class Solution:
    def InversePairs(self, data):
        global count

        def MergeSort(lists):
            global count
            if len(lists) <= 1:
                return lists
            num = int(len(lists) / 2)
            left = MergeSort(lists[:num])
            right = MergeSort(lists[num:])
            r, l = 0, 0
            result = []
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
                    count += len(left) - l
            result += right[r:]
            result += left[l:]
            return result

        MergeSort(data)
        return count % 1000000007

# 以下解法O(n^2)
# class Solution:
#    def InversePairs(self, data):
#        # write code here
#        n = len(data)
#        if len(data) == 0:
#            return 0
#        P = 0
#        i = 1
#        while n:
#            com = data[-i]
#            com_data = data[::-1][i:]
#            for val in com_data:
#                if val > com:
#                    P += 1
#            i += 1
#            n -= 1
#        return P%1000000007