from typing import List


def findMin(nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        res = float("inf")
        while left < right:
            mid = (left + right) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

        return min(res, nums[left])