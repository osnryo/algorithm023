# 42. 接雨水
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水

class Solution(object):
    def trap(self, bars):
        if not bars or len(bars) < 3:
            return 0
        volume = 0
        left, right = 0, len(bars) - 1
        l_max, r_max = bars[left], bars[right]
        while left < right:
            l_max, r_max = max(bars[left], l_max), max(bars[right], r_max)
            if l_max <= r_max:
                volume += l_max - bars[left]
                left += 1
            else:
                volume += r_max - bars[right]
                right -= 1
        return volume


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # "两头大小决定中间"的题目，考虑使用单调栈来解决，
        # 类似于84题"柱状图中最大矩形"，但注意两题中所求面积不同导致的代码差异，84题求各最大值，而本题求和
        stack = []            # 欲维护一个递减栈，注意我们的栈中保存元素下标
        res = 0

        for i in range(len(height)):

            # 新比较的元素比栈顶元素大 ---> 栈顶元素的右边界已找到，
            # 又因为我们维护了一个递减栈，栈顶下面的元素高度也大于他，即栈顶处形成凹陷，可计算面积
            while stack and height[i] > height[stack[-1]]:

                # 记录栈顶的元素并出栈，接下来我们已经得知栈顶的左右边界，可计算此元素的面积
                top = stack.pop()
                if not stack: break          # 把栈顶弹出后栈空，即其左边没有比他大的了，无法接水

                # 栈顶值面积，宽: 右(即为新比较的元素) - 左(弹出后stack-1即为其左) - 1
                # 长：左右高柱中较矮的柱子  - 栈顶高度
                # 每次面积实际上仅仅是"本元素可接的水的面积"，又因为出栈，不会重复计算， += 计算总面积。相关面积可参考甜姨动图理解
                res += (i - stack[-1] - 1) * (min(height[i], height[stack[-1]]) - height[top])

            stack.append(i)           # 新比较的元素比栈顶元素矮 ---> 未找到右边界，没形成凹陷。 将新比较的元素入该单减栈
        return res