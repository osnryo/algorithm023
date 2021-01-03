# 66. 加一
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
# 你可以假设除了整数 0 之外，这个整数不会以零开头。

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    #     count = 0
    #     # 需要保持前置0的个数 [0,0] -> [0,1]
    #     for i in range(len(digits)-1):
    #         if digits[i]:
    #             break
    #         count += 1
    #     num = int("".join([str(x) for x in digits])) + 1
    #     return [0] * count + [int(x) for x in list(str(num))]
        
        # 逢9进一 time:最好O(1)，最坏O(n) space:O(1)
        digits = [0] + digits
        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
        if digits[0] == 0:
            return digits[1:] 
        else:
            return digits