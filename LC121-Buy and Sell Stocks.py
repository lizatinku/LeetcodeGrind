# My plan

# set buying day and selling day to be the first element of array 
# set maximum profit to be 0
# for loop through the array
# if you find a lower price, set as buying day and selling day
# if you find a higher price, set as selling day
# calculate current profit which is selling day - buying day
# compare current and max profit, and if higher, set as new maximum profit
# return the maximum profit


# Concept: The key idea here is that when you find a lower price, you reset both buying_day and selling_day to this lower price because it represents a new baseline for your potential transactions. 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buying_day = prices[0]
        selling_day = prices[0]
        max_profit = 0

        for i in prices:
            if i < buying_day:
                buying_day = i
                selling_day = i
            else:
                selling_day = i
            
            current_profit = selling_day - buying_day
            if current_profit > max_profit:
                max_profit = current_profit
            
        return max_profit
