# 242. 有效的字母异位词 
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

class Solution:
    def isAnagram1(self, s, t):
    dic1, dic2 = {}, {}
    for item in s:
        dic1[item] = dic1.get(item, 0) + 1
    for item in t:
        dic2[item] = dic2.get(item, 0) + 1
    return dic1 == dic2
    
    def isAnagram2(self, s, t):
        dic1, dic2 = [0]*26, [0]*26
        for item in s:
            dic1[ord(item)-ord('a')] += 1
        for item in t:
            dic2[ord(item)-ord('a')] += 1
        return dic1 == dic2
    
    def isAnagram3(self, s, t):
        return sorted(s) == sorted(t)
        
