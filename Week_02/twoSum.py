# 1. 两数之和
# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，
# 并返回它们的数组下标。

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset={}
        for i in range(len(nums)):
            if hashset.get(target-nums[i]) is not None :
                return [hashset.get(target-nums[i]),i]
            hashset[nums[i]]=i