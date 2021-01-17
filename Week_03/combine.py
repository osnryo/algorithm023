  
"""
77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
"""


class Solution:  
    def combine(self, n, k):
        if k == 0:
            return [[]]
        return [pre + [i] for i in range(k, n+1) for pre in self.combine(i-1, k-1)]


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        #生成数
        nums = [i for i in range(1,n+1)]

        #回溯
        res = []

        def backtrace(nums_b,curr_res,index):
            # print("curr_res:",curr_res)
            if len(curr_res)==k:
                res.append(curr_res[:]) #浅拷贝
                return

            for i in range(index,n):
                # print(i,nums_b)
                curr_res.append(nums[i])
                backtrace(nums_b[index:],curr_res,i+1)
                curr_res.pop()

        #特殊处理
        if n==0 or k==0:
            return res

        backtrace(nums,[],0)
        return res