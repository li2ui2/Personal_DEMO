"""
将像"I am a student."这样的字符串进行翻转，翻转后结果为："student. a am I"。
思路：先转单词，再转句子。
"""


def reverse(words):
    for i in range(len(words) >> 1):
        words[i], words[-i - 1] = words[-i - 1], words[i]
    return words


def ReverseSentence(s):
    # write code here
    wordstart = 0
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ':
            s[wordstart:i] = reverse(s[wordstart:i])
            wordstart = i + 1
    s[wordstart:] = reverse(s[wordstart:])
    s = reverse(s)
    return ''.join(s)


def ReverseSentence2(s):
    # write code here
    s = s.split(" ")
    return " ".join(s[::-1])


if __name__ == '__main__':
    s = "I am a student."
    print(ReverseSentence(s))
    print(ReverseSentence2(s))

