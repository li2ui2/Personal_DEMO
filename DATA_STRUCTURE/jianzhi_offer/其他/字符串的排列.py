"""
输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,
则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
"""


class Solution:
    def Permutation(self, ss):
        # write code here
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
            ans = self.Permutation(ss[:i]+ss[i+1:])
            for k in ans:
                ret.append(ss[i:i+1]+k)
        return ret
