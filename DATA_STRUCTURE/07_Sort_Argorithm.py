def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    # 升序
    for j in range(n-1):
        count = 0  # 用于计数每次遍历的交换次数
        for i in range(n-1-j):
            # 从头走到尾一次
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if count == 0:
            # 若当前一次遍历结束后，若没进行交换，则说明已排好顺序了
            break


def select_sort(alist):
    """选择排序"""
    n = len(alist)
    # 升序
    # 需要进行n-1次选择操作
    for j in range(n-1):
        # 记录最小值索引
        min_index = j
        for i in range(j+1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        # 如果选择出的数据不在正确位置，进行交换
        if min_index != j:
            alist[j], alist[min_index] = alist[min_index], alist[j]


def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    # 从右边的无序序列中取出多少个元素执行这样的过程
    for j in range(1, n):
        # i代表内层循环的起始值
        i = j
        # 执行从右边的无序序列中取出第一个元素，即i位置的元素，
        # 然后将其插入到前面的正确位置中。
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            else:
                break


def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2
    # gap变化到0之前，插入算法执行的次数
    while gap >= 1:
        # 插入算法与普通的插入算法的区别就是gap步长
        for j in range(gap, n):
            i = j
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        # 缩短gap步长
        gap //= 2


def main():
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # bubble_sort(li)
    # print("冒泡排序结果：", li)
    # select_sort(li)
    # print("选择排序结果：", li)
    # insert_sort(li)
    # print("插入排序结果：", li)
    shell_sort(li)
    print("希尔排序结果：", li)


if __name__ == "__main__":
    main()
