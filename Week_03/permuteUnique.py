"""
47. 全排列 II
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
"""

# To find the last index for inserting new number n into old permutation p, 
# I search for previous instances of n in p. 
# But because index throws an exception if unsuccessful, 
# I add a sentinel n at the end (which is the appropriate last insertion index then).

def permuteUnique(self, nums):
    perms = [[]]
    for n in nums:
        perms = [p[:i] + [n] + p[i:]
                 for p in perms
                 for i in xrange((p + [n]).index(n) + 1)]
    return perms

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.res = []
        check = [0 for i in range(len(nums))]
        
        self.backtrack([], nums, check)
        return self.res
        
    def backtrack(self, sol, nums, check):
        if len(sol) == len(nums):
            self.res.append(sol)
            return
        
        for i in range(len(nums)):
            if check[i] == 1:
                continue
            if i > 0 and nums[i] == nums[i-1] and check[i-1] == 0:
                continue
            check[i] = 1
            self.backtrack(sol+[nums[i]], nums, check)
            check[i] = 0

