import itertools


def Permutation(ss):
    """剑指offer：字符串的排列"""
    n = len(ss)
    if n == 0:
        return []
    if n == 1:
        return [ss]
    ret = []
    pre = None
    for i in range(n):
        if pre == ss[i]:
            continue
        else:
            pre = ss[i]
        ans = Permutation(ss[:i] + ss[i + 1:])
        for k in ans:
            ret.append(ss[i:i + 1] + k)
    return ret


# def PrintMinNumber(numbers):
#
#     def Permutation(ss):
#         n = len(ss)
#         if n == 0:
#             return []
#         if n == 1:
#             return [ss]
#         ret = []
#         pre = None
#         for i in range(n):
#             if pre == ss[i]:
#                 continue
#             else:
#                 pre = ss[i]
#             ans = Permutation(ss[:i] + ss[i + 1:])
#             for k in ans:
#                 ret.append(ss[i:i + 1] + k)
#         return ret
#     num = list(map(str, numbers))
#     temp = Permutation(num)
#     ret = []
#     for i in range(len(temp)):
#         ret.append(int(''.join(temp[i])))
#
#     return min(ret)

def PrintMinNumber(numbers):
    # write code here
    if not numbers:
        return ''
    nums = []
    list_num = list(itertools.permutations(numbers, len(numbers)))
    for item in list_num:
        num = ''.join(map(str, item))
        nums.append(num)
    return min(map(int, nums))


if __name__ == '__main__':
    ss = "ABC"
    list_ss = list(itertools.permutations(ss))
    print(Permutation("ABC"))
    # numbers = [3, 5, 1, 4, 2]
    # print(PrintMinNumber(numbers))
