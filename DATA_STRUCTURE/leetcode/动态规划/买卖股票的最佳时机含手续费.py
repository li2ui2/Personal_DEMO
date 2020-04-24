"""
leetcode714
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。
注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。
例子：
输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxProfit(self, prices, fee):
        # cash, hold = 0, -prices[0]
        # for i in range(1, len(prices)):
        #     cash = max(cash, hold + prices[i] - fee)
        #     hold = max(hold, cash - prices[i])
        # return cash
        n = len(prices)
        dpi_0 = 0
        dpi_1 = float("-inf")
        for i in range(n):
            temp = dpi_0
            dpi_0 = max(dpi_0, dpi_1 + prices[i] - fee)
            dpi_1 = max(dpi_1, temp - prices[i])
        return dpi_0


if __name__ == '__main__':
    s = Solution()
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(s.maxProfit(prices, fee))
