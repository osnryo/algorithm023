class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # 首先判断数组是否小于4
        if len(nums) < 4:
            return []
        
        # 排序        
        nums.sort()
        
        # 遍历找第一个数，时间复杂度n
        for i in range(len(nums) - 3):
            
            # 跳过重复的数
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 跳过不成功的数
            if nums[i] * 4 > target:
                break
                
            # 遍历找第二个数，时间复杂度n
            for j in range(i + 1, len(nums) -2):
                
                # 跳过重复的数
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                # 跳过不成功的数
                if nums[j] *3 > target - nums[i]:
                    break
                
                # 找最后两个数，跟2数之和和三数之和问题一样
                l, r = j + 1, len(nums) - 1
                
                while l < r:
                    
                    s = nums[i] + nums[j] + nums[l] +nums[r]
                    if s > target:
                        r = r - 1
                    elif s < target:
                        l = l + 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]:
                            l = l + 1
                        while l < r and nums[r] == nums[r - 1]:
                            r = r - 1
                        l, r = l + 1, r - 1
                        
        return res