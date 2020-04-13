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


def quick_sort(alist, start, end):
    """快速排序"""
    # 递归的退出条件
    if start >= end:
        return

    mid_value = alist[start]  # 设定起始元素为要寻找位置的基准元素

    low = start   # low为序列左边的由左向右移动的游标
    high = end   # high为序列右边的由右向左移动的游标

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] >= mid_value:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid_value:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素(mid_value)的正确位置
    # 将基准元素放到该位置
    alist[low] = mid_value
    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low-1)
    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low+1, end)


def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    mid = len(alist) // 2
    left_list = merge_sort(alist[:mid])
    right_list = merge_sort(alist[mid:])

    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_list) \
            and right_pointer < len(right_list):
        if left_list[left_pointer] <= right_list[right_pointer]:
            result.append(left_list[left_pointer])
            left_pointer += 1
        else:
            result.append(right_list[right_pointer])
            right_pointer += 1
    result += left_list[left_pointer:]
    result += right_list[right_pointer:]

    return result


def main():
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # bubble_sort(li)
    # print("冒泡排序结果：", li)
    # select_sort(li)
    # print("选择排序结果：", li)
    # insert_sort(li)
    # print("插入排序结果：", li)
    # shell_sort(li)
    # print("希尔排序结果：", li)
    quick_sort(li, 0, len(li)-1)
    print("快速排序结果：", li)
    # result = merge_sort(li)
    # print("归并排序结果：", result)


if __name__ == "__main__":
    main()
