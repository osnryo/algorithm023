"""
455. 分发饼干
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
"""
class Solution(object):
    def findContentChildren(self, g, s):
        # 先排序两个集合
        g.sort()
        s.sort()
        
        childi = 0
        cookiei = 0
        
        # 饼干数和孩子数在长度内时
        while cookiei < len(s) and childi < len(g):
            if s[cookiei] >= g[childi]: #饼干数大于孩子需求数时，被满足的孩子加1
                childi += 1 
            cookiei += 1
        
        return childi