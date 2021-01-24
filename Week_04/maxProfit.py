"""
122. 买卖股票的最佳时机 II
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""

# 贪心算法
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # 遍历整个股票交易日价格列表
        for i in range(1, len(prices)):
            # 所有上涨交易日都买卖（赚到所有利润），所有下降交易日都不买卖（永不亏钱）。
            tmp = prices[i] - prices[i - 1] 
            if tmp > 0: profit += tmp # 前一天的价格比后一天高时计算为收益
        return profit #总利润 profit


class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 1: # edge case
            return 0 
        # take down positive daily return only
        profit = [] 
        for i in range(1, len(prices)):
            profit.append(max(0, prices[i] - prices[i-1])) 
        return sum(profit)

