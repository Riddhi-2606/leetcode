
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        # Find minimum price
        min_price = min(price for factor, price in items)

        # Count frequency of each factor
        max_factor = max(factor for factor, price in items)
        freq = [0] * (max_factor + 1)

        for factor, price in items:
            freq[factor] += 1

        # Count how many other item types each factor can unlock
        gain = [0] * (max_factor + 1)

        for f in range(1, max_factor + 1):
            count = 0
            for multiple in range(f, max_factor + 1, f):
                count += freq[multiple]

            gain[f] = count - 1

        # Sort items by price
        items.sort(key=lambda x: x[1])

        remaining = budget
        boosted = 0

        # Buy items that provide an additional free item
        for factor, price in items:

            if price > 2 * min_price:
                break

            if remaining < price:
                break

            take = min(gain[factor], remaining // price)

            boosted += take
            remaining -= take * price

        # Spend remaining budget on cheapest items
        return 2 * boosted + remaining // min_price
