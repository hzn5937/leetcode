from typing import List


def findDuplicate(nums: List[int]) -> int:
    slow, fast = 0, 0
    # find the intersection point of the two runners
    # Since there is a duplicate and the array will never get out of bound, the two runners will meet

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # find the "entrance" to the cycle = duplicated number
    # As explain below distance from start to entrance = distance from intersection to entrance
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow

# start of the array to cycle entrance = d
# cycle entrance to intersection = x
# cycle = c
# 2 * slow = fast
# at intersection: fast = d + nc - x
# at intersection: slow = d + c - x
# => 2 * (d + c - x) = d + nc - x
# => 2d + 2c - 2x = d + nc - x
# => d + (2-n)c = x
# For most of the time n == 2 so d = x


print(findDuplicate([1,3,4,2,2]))  # 2