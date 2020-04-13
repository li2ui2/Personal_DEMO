"""
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，
则最小的4个数字是1,2,3,4。
"""


class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        # 创建最大堆
        def create(num):
            heap.append(num)
            index = len(heap) - 1
            while index != 0:
                parentIndex = (index - 1) // 2
                if heap[parentIndex] < heap[index]:
                    heap[parentIndex], heap[index] = heap[index], heap[parentIndex]
                    index = parentIndex
                else:
                    break

        # 调整最大堆， 改变头节点的值
        def adjust(num):
            if num < heap[0]:
                heap[0] = num
            index = 0
            heapLen = len(heap)
            while index < heapLen:
                left = index * 2 + 1
                right = index * 2 + 2
                largeIndex = 0
                if right < heapLen:
                    if heap[right] < heap[left]:
                        largeIndex = left
                    else:
                        largeIndex = right
                elif left < heapLen:
                    largeIndex = left
                else:
                    break
                if heap[index] < heap[largeIndex]:
                    heap[index], heap[largeIndex] = heap[largeIndex], heap[index]
                index = largeIndex

        heap = []  # 用于存储堆数据

        inputLen = len(tinput)
        if inputLen < k or k <= 0:
            return []

        for i in range(inputLen):
            if i < k:
                create(tinput[i])
            else:
                adjust(tinput[i])
        heap.sort()
        return heap