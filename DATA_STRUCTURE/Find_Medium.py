class Solution:
    """
        剑指offer：求数据流中的中位数，
        即每Insert一个num，求一次最新序列的GetMedian
    """
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

    def GetMedian(self):
        # write code here
        if self.minHeapCount < self.maxHeapCount:
            return self.maxHeap[0]
        else:
            return float(self.maxHeap[0] + self.minHeap[0]) / 2

    def creatMaxHeap(self, num):
        self.maxHeap.append(num)
        curIndex = len(self.maxHeap) - 1
        while curIndex != 0:
            curParentIndex = (curIndex - 1) // 2
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
            curParentIndex = (curIndex - 1) // 2
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


if __name__ == '__main__':
    s = Solution()
    for i in [5, 2, 3, 4, 1, 6, 7, 0, 8]:
        s.Insert(i)
        print(s.GetMedian())
