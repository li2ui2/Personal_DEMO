from collections import Counter


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        print("开始")
        k = []
        result = []
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i + 1:]):
                for _, c in enumerate(nums[j + i + 2:]):
                    if a + b + c == 0 and Counter([a, b, c]) not in k:
                        k.append(Counter([a, b, c]))
        for i in k:
            result.append(list(i.elements()))
        return result


def main():
    input_data = []
    for i in range(6):
        a = input("请输入一个整数：")
        input_data.append(int(a))

    print(input_data)
    solution = Solution()
    result = solution.threeSum(input_data)
    # for index in result:
    #     print(index)
    print(result)


if __name__ == "__main__":
    main()
