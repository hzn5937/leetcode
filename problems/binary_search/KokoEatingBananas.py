import math
from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    left, right = 1, max(piles)
    res = right

    while left <= right:
        k = (left + right) // 2

        total_time = 0
        for pile in piles:
            total_time += math.ceil(float(pile) / k)
        if total_time <= h:
            res = k
            right = k - 1
        else:
            left = k + 1

    return res


print(minEatingSpeed([3, 6, 7, 11], 8))  # 4
print(minEatingSpeed([30, 11, 23, 4, 20], 5))  # 30
print(minEatingSpeed([30, 11, 23, 4, 20], 6))  # 23

