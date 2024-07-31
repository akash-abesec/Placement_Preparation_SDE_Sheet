Problem :- https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Solution :- https://www.youtube.com/watch?v=excAOvwF_Wk&ab_channel=takeUforward

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            
            profit = max(profit, p - buy_price)
        
        return profit
