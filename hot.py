
"""
    两数之和
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    ret = twoSum(nums, target)
    print(ret)
