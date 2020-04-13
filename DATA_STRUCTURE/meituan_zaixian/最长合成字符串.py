"""
最长合成字符串：
有一组单词，请编写一个程序，在数组中找出由数组中字符串组成的最长的串A，
即A是由其它单词组成的(可重复)最长的单词。
给定一个string数组str，同时给定数组的大小n。
请返回最长单词的长度，保证题意所述的最长单词存在。
测试样例：
["a","b","c","ab","bc","abc"],6
返回：3
"""


class LongestString:
    def getLongest(self, s, n):
        m = {k: True for k in s}
        s.sort(key=lambda k: len(k), reverse=True)  # 按从长到短的单词进行排序
        # 循环判断每个单词能否由其他单词组成
        for i in range(n):
            # 初始传入一个true，如果这个单词不能构成，下面会优化成false
            if self.f(s[i], m, True):
                return len(s[i])

    def f(self, k, m, b):
        # 如果是false，就直接检查返回了
        if not b and k in m:
            return m[k]
        for i in range(1, len(k)):
            if self.f(k[0:i], m, False) and self.f(k[i:], m, False):
                return True
        m[k] = False
        return False