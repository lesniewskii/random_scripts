class Solution:
    
    def maxProfit(self, prices):
        l = 0 
        r = 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP

sol = Solution() 
print(sol.maxProfit([1,2,3,4,5]))


#second solution


prices = [1,2,3,4,5]
l = 0
maxPrice1 = 0
for r in range(1, len(prices)):
    if prices[r] > prices[l]:
        profit = prices[r] - prices[l]
        maxPrice1 = max(maxPrice1, profit)
    else:
        l = r
print(maxPrice1)