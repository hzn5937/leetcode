from typing import List


def findDuplicate(nums: List[int]) -> int:
    slow, fast = 0, 0
    # find the intersection point of the two runners
    # Since there is a duplicate and the array will never get out of bound, the two runners will meet
    # What special about this intersection:
    # The distance from the start of the array to the intersection point is equal to the distance from the start of the cycle to the intersection point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # find the "entrance" to the cycle
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow

print(findDuplicate([1,2,3,4,5]))  # 2