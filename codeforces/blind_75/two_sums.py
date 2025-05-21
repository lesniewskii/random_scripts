nums = [2, 7, 11, 15]
target = 9
prev = {}

class Solution:
    def twoSum(self, nums: int, target: int):
        prev = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev:
                return [prev[diff], i]
            prev[n] = i
        return