# Best Time to Buy and Sell Stock II

import math 

class Solution:
  def maxProfit(self, prices: list[int]) -> int:
    sell = 0
    hold = -math.inf

    for price in prices:
      sell = max(sell, hold + price)
      hold = max(hold, sell - price)

    return sell


# Сложность составляет: O(n);