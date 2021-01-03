# 旋转数组
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

# Time complexity: O(N)
# Space complexity: O(N)
# Python slice create new array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return
        nums[:-k], nums[-k:] = nums[-k:], nums[:-k]
        return


# Time complexity: O(NK)
# Space complexity: O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        while k:
            nums.insert(0, nums.pop())
            k -= 1