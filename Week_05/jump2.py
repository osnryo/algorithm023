class Solution:
    def jump(self, nums: List[int]) -> int:
        # 广度优先搜索算法
        # 设置start和end保存开始节点的当前范围
        n, start, end, step = len(nums), 0, 0, 0
        
        #只要没到最后一个位置就一直跳
        while end < n - 1:
            
            step += 1 #计算跳了几步
            maxend = end + 1
            
            #每次都将范围内的索引遍历一遍，找到跳跃的最大长度
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
                
            #每次移动后将start更新为end+1，end更新为当前[start,end]中最远可到达的索引
            start, end =  end + 1, maxend
            
        return step
        
        