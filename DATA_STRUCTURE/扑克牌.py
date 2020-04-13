import collections
def poker_playing(nums):
    nums_list = []
    for i, val in enumerate(nums):
        nums_list.extend(val * [i+1])
    count = collections.Counter(nums_list)
    left = 0
    shun = []
    dui = []
    ret = 0
    for right, val in enumerate(nums):
        pass

    return ret


if __name__ == '__main__':
    nums = list(map(int, input().split()))
    ret = poker_playing(nums)
    print(ret)
