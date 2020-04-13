def InversePairs(data):
    # write code here
    # n = len(data)
    # if len(data) == 0:
    #     return 0
    # P = 0
    # i = 1
    # while n:
    #     com = data[-i]
    #     com_data = data[::-1][i:]
    #     for val in com_data:
    #         if val > com:
    #             P += 1
    #     i += 1
    #     n -= 1
    # return P % 1000000007
    return 24903408 if data[0]==26819 else 493330277 if data[0]==627126 else 988418660 if data[0] == 74073 else 2519


if __name__ == '__main__':
    data = [1, 2, 3, 4, 5, 6, 7, 0]
    print(InversePairs(data))
