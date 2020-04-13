def LCS(string1,string2):
    """找最长公共子序列"""
    len1 = len(string1)
    len2 = len(string2)
    res = [[0 for i in range(len1+1)] for j in range(len2+1)]
    result_str = []
    for i in range(1, len2+1):
        for j in range(1, len1+1):
            if string2[i-1] == string1[j-1]:
                res[i][j] = res[i-1][j-1]+1
                # result_str.append(string2[i-1])
            else:
                res[i][j] = max(res[i-1][j], res[i][j-1])
    return res[-1][-1], "".join(result_str)


def LCstring(string1, string2):
    """找最长公共子串"""
    len1 = len(string1)
    len2 = len(string2)
    res = [[0 for i in range(len1+1)] for j in range(len2+1)]
    result = 0
    result_str = []
    for i in range(1, len2+1):
        for j in range(1, len1+1):
            if string2[i-1] == string1[j-1]:
                res[i][j] = res[i-1][j-1]+1
                result = max(result, res[i][j])
    for i in range(len1):
        if string1[i: i+result] in string2:
            result_str = string1[i: i+result]
            break
    return result, "".join(result_str)


if __name__ == '__main__':
    s = "abcbcb"
    ss = s[::-1]
    # ret = find_max("abcbcb")
    ret = LCstring(s, ss)
    # ret = LCS("helloworld", "loop")
    print(ret[0], ret[1])
