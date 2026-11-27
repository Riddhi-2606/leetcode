from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        # Step 1: Count frequency of each factor (1 <= factor <= 1500)
        max_factor = max(factor for factor, _ in items)
        freq = [0] * (max_factor + 1)
        for factor, _ in items:
            freq[factor] += 1

        # Precompute total multiples for every factor in O(M log M)
        multiples_count = [0] * (max_factor + 1)
        for f in range(1, max_factor + 1):
            if freq[f] > 0:
                for multiple in range(f, max_factor + 1, f):
                    multiples_count[f] += freq[multiple]

        # Step 2: 0/1 Knapsack for the FIRST purchase of each item
        # Buying item i for the first time gives: 1 (itself) + (multiples_count[factor] - 1) free items
        dp = [0] * (budget + 1)
        min_price = float('inf')

        for factor, price in items:
            if price < min_price:
                min_price = price
            if price > budget:
                continue

            first_buy_gain = multiples_count[factor]
            for b in range(budget, price - 1, -1):
                if dp[b - price] + first_buy_gain > dp[b]:
                    dp[b] = dp[b - price] + first_buy_gain

        # Step 3: Spend any remaining budget on the cheapest item (+1 copy per purchase)
        ans = 0
        for b in range(budget + 1):
            extra_copies = (budget - b) // min_price
            ans = max(ans, dp[b] + extra_copies)

        return ans
        