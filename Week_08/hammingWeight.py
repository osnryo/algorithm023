"""
191. 位1的个数
编写一个函数，输入是一个无符号整数（以二进制串的形式），
返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。
"""

# 方法一：基于位运算 与（&）操作
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        counter = 0
    
        while n:
            
            # 利用位运算性质，num & (num -1) 能把最后一位1消掉
            # this will take out the right-most 1 of n    
            n = n & (n-1)
            
            # update counter
            counter += 1
        
        return counter

# 方法二：基于位运算 右移（>>）操作
# 右移是所有的位向右移，丢掉地位，相当于除以2^n
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        num_of_1s = 0
        
        for i in range(64):
            
            num_of_1s += (n & 1)
            
            n = n >> 1
            
        return num_of_1s


# 方法三：使用系统函数
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
        