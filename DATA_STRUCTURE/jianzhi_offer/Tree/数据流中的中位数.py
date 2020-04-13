"""
如何得到一个数据流中的中位数？
如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
"""


class Solution:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        self.maxHeapCount = 0
        self.minHeapCount = 0

    def Insert(self, num):
        # write code here
        if self.maxHeapCount > self.minHeapCount:
            self.minHeapCount += 1
            if num < self.maxHeap[0]:
                temp = self.maxHeap[0]
                self.adjustMaxHeap(num)
                self.creatMinHeap(temp)
            else:
                self.creatMinHeap(num)
        else:
            self.maxHeapCount += 1
            if len(self.maxHeap) == 0:
                self.creatMaxHeap(num)
            else:
                if num > self.minHeap[0]:
                    temp = self.minHeap[0]
                    self.adjustMinHeap(num)
                    self.creatMaxHeap(temp)
                else:
                    self.creatMaxHeap(num)

    def GetMedian(self, n=None):
        # write code here
        if self.minHeapCount < self.maxHeapCount:
            return self.maxHeap[0]
        else:
            return float(self.maxHeap[0] + self.minHeap[0]) / 2

    def creatMaxHeap(self, num):
        self.maxHeap.append(num)
        curIndex = len(self.maxHeap) - 1
        while curIndex != 0:
            curParentIndex = (curIndex - 1) >> 1
            if self.maxHeap[curParentIndex] < self.maxHeap[curIndex]:
                self.maxHeap[curParentIndex], self.maxHeap[curIndex] = self.maxHeap[curIndex], self.maxHeap[
                    curParentIndex]
                curIndex = curParentIndex
            else:
                break

    def creatMinHeap(self, num):
        self.minHeap.append(num)
        curIndex = len(self.minHeap) - 1
        while curIndex != 0:
            curParentIndex = (curIndex - 1) >> 1
            if self.minHeap[curParentIndex] > self.minHeap[curIndex]:
                self.minHeap[curParentIndex], self.minHeap[curIndex] = self.minHeap[curIndex], self.minHeap[
                    curParentIndex]
                curIndex = curParentIndex
            else:
                break

    def adjustMaxHeap(self, num):
        if num < self.maxHeap[0]:
            self.maxHeap[0] = num
        curIndex = 0
        maxHeapLen = len(self.maxHeap)
        while curIndex < maxHeapLen:
            curLeftIndex = curIndex * 2 + 1
            curRightIndex = curIndex * 2 + 2
            largeIndex = 0
            if curRightIndex < maxHeapLen:
                if self.maxHeap[curLeftIndex] < self.maxHeap[curRightIndex]:
                    largeIndex = curRightIndex
                else:
                    largeIndex = curLeftIndex
            elif curLeftIndex < maxHeapLen:
                largeIndex = curLeftIndex
            else:
                break
            if self.maxHeap[curIndex] < self.maxHeap[largeIndex]:
                self.maxHeap[curIndex], self.maxHeap[largeIndex] = self.maxHeap[largeIndex], self.maxHeap[curIndex]
            curIndex = largeIndex

    def adjustMinHeap(self, num):
        if num > self.minHeap[0]:
            self.minHeap[0] = num
        curIndex = 0
        minHeapLen = len(self.minHeap)
        while curIndex < minHeapLen:
            curLeftIndex = curIndex * 2 + 1
            curRightIndex = curIndex * 2 + 2
            smallIndex = 0
            if curRightIndex < minHeapLen:
                if self.minHeap[curLeftIndex] > self.minHeap[curRightIndex]:
                    smallIndex = curRightIndex
                else:
                    smallIndex = curLeftIndex
            elif curLeftIndex < minHeapLen:
                smallIndex = curLeftIndex
            else:
                break
            if self.minHeap[curIndex] > self.minHeap[smallIndex]:
                self.minHeap[curIndex], self.minHeap[smallIndex] = self.minHeap[smallIndex], self.minHeap[curIndex]
            curIndex = smallIndex