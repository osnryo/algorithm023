"""
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
"""

# 深度优先搜索
def permute(self, nums):
    res = []
    self.dfs(nums, [], res)
    return res
    
def dfs(self, nums, path, res):
    if not nums:
        res.append(path)
        # return # backtracking
    for i in xrange(len(nums)):
        self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

# Insert the first number anywhere in any permutation of the remaining numbers.
def permute(self, nums):
    return nums and [p[:i] + [nums[0]] + p[i:]
                     for p in self.permute(nums[1:])
                     for i in range(len(nums))] or [[]]