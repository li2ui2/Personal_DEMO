import collections


def lengthOfLongestSubstring(s):
    """找字符串s中的最长子串"""
    # 方法一
    res = 0  # 存储历史循环中最长的子串长度
    if s is None or len(s) == 0:
        return res
    store_dict = {}  # 定义一个字典，存储不重复的字符和字符所在的下标
    head = 0  # 头指针
    cur_max = 0  # 存储每次循环中最长的子串长度
    for tail in range(len(s)):
        # 判断当前字符是否在字典中和当前字符的下标是否大于等于最近重复字符的所在位置
        if s[tail] in store_dict and store_dict[s[tail]] >= head:
            head = store_dict[s[tail]] + 1  # 头指针移动，值+1
        # 在此次循环中，最大的不重复子串的长度
        cur_max = tail - head + 1
        # 把当前位置覆盖字典中的位置
        store_dict[s[tail]] = tail
        # 比较此次循环的最大不重复子串长度和历史循环最大不重复子串长度
        res = max(res, cur_max)

    return res

    # 方法二
    # if len(s) == 0 or s == "":
    #     return 0
    # dict_s = collections.Counter()
    # left = 0
    # result = 0
    # cru_result = 0
    # for right in range(len(s)):
    #     dict_s[s[right]] += 1
    #     # cru_result += 1
    #     cru_result = right - left + 1
    #     if dict_s[s[right]] > 1:
    #         cru_result -= 1
    #     while dict_s[s[right]] > 1:
    #         dict_s[s[left]] -= 1
    #         left += 1
    #     result = max(cru_result, result)
    # return result


def minWindow(s, t):
    """
        leetcode76
        以下解法可行，但是超出时间限制
    """
    if len(s) < len(t):
        return ""
    # if t in s:
    #     return t
    # count = collections.Counter()
    # count2 = collections.Counter(t)
    # left = 0
    # curLength = 0
    # resultLength = 0
    # result = ""
    # for right in range(len(s)):
    #     count[s[right]] += 1
    #     while all(count[c] >= count2[c] for c in t):
    #         curLength = right - left + 1
    #         if resultLength == 0:
    #             result = s[left: right+1]
    #             resultLength = curLength
    #         if curLength < resultLength:
    #             result = s[left: right+1]
    #             resultLength = curLength
    #         count[s[left]] -= 1
    #         left += 1
    #         if left > len(s)-1:
    #             break
    #         while s[left] not in t:
    #             count[s[left]] -= 1
    #             left += 1
    #             if left > len(s)-1:
    #                 break
    # return result
    dict_t = collections.Counter(t)
    required = len(dict_t)
    left, right = 0, 0
    formed = 0
    window_counts = {}
    ans = float("inf"), None, None
    while right < len(s):
        character = s[right]
        window_counts[character] = window_counts.get(character, 0) + 1
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1
        # Try and co***act the window till the point where it ceases to be 'desirable'.
        while left <= right and formed == required:
            character = s[left]
            # Save the smallest window until now.
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            # The character at the position pointed by the `left` pointer is no longer a part of the window.
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1
            # Move the left pointer ahead, this would help to look for a new window.
            left += 1
        # Keep expanding the window once we are done co***acting.
        right += 1
    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


def minWindow2(s, t):
    if len(s) < len(t):
        return ""
    str_count = collections.Counter(t)
    left = 0
    count = len(t)
    maxLength = len(s) + 1
    result = ""
    for right in range(len(s)):
        str_count[s[right]] -= 1
        if str_count[s[right]] >= 0:
            count -= 1
        while left < right and str_count[s[left]] < 0:
            str_count[s[left]] += 1
            left += 1

        if count == 0 and maxLength > right - left + 1:
            maxLength = right - left + 1
            result = s[left: right+1]
    return result


def findAnagrams(s, p):
    """找字符串中所有字母异位词，leetcode 438"""
    if s == [] or p == [] or len(s) < len(p):
        return []

    counts = collections.Counter()
    countp = collections.Counter(p)

    left = 0
    result = []
    cur_length = 0
    plength = len(p)
    for right in range(len(s)):
        counts[s[right]] += 1
        if counts[s[right]] > 0:
            cur_length += 1

        if s[right] not in countp:
            counts.clear()
            cur_length = 0
            left = right + 1
        if cur_length == plength:
            if counts == countp:
                result.append(left)
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
                cur_length -= 1
            elif counts != countp:
                counts[s[left]] -= 1
                if counts[s[left]] == 0:
                    del counts[s[left]]
                left += 1
                cur_length -= 1
    return result


def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    s_dict = collections.Counter(s1)

    left = 0
    tempLen = 0
    s1Len = len(s1)
    result = False
    for right in range(len(s2)):
        s_dict[s2[right]] -= 1
        if s_dict[s2[right]] >= 0:
            tempLen += 1
        if right >= s1Len:
            s_dict[s2[left]] += 1
            if s_dict[s2[left]] >= 1:
                tempLen -= 1
            left += 1
        if tempLen == s1Len:
            return True
    return result


def subarraysWithKDistinct(A, K):
    if len(A) == 0 or K <= 0:
        return 0
    # 滑动窗口求解
    count = collections.Counter()
    left = 0
    result = 1
    results = 0
    ok = 0
    for right in range(len(A)):
        count[A[right]] += 1
        if count[A[right]] == 1:
            ok += 1
        while count[A[left]] > 1 or ok > K:
            if ok > K:
                ok -= 1
                result = 1
            else:
                result += 1
            count[A[left]] -= 1
            left += 1
        if ok == K:
            results += result
    return results


def characterReplacement(s, k):
    """
        leetcode424：求替换后的最长重复字符
        当k=0时，相当于求解最长连续子串长度的问题
    """
    if len(s) == 0 or s is None:
        return 0
    count = collections.Counter()
    left = 0
    result = 0
    cur_max = 0
    for right in range(len(s)):
        count[s[right]] += 1
        cur_max = max(cur_max, count[s[right]])
        while right - left + 1 - cur_max > k:
            count[s[left]] -= 1
            left += 1
        result = max(right - left + 1, result)
    return result


if __name__ == '__main__':
    # s = "abcabcbb"
    # ret = lengthOfLongestSubstring(s)
    # A = [1, 2, 1, 3, 4]
    # K = 3
    # ret = subarraysWithKDistinct(A, K)
    # s = "abab"
    # p = "ab"
    # ret = findAnagrams(s, p)
    # s = "abcabdebac"
    # t = "cda"
    # ret = minWindow2(s, t)
    # s1 = "ab"
    # s2 = "eidbaooo"
    # ret = checkInclusion(s1, s2)
    # A = [1, 2, 1, 2, 3]
    # K = 2
    # ret = subarraysWithKDistinct(A, K)
    s = "abbbbbbcccdd"
    k = 0
    ret = characterReplacement(s, k)
    print(ret)
