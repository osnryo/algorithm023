"""
127. 单词接龙
字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列：

序列中第一个单词是 beginWord 。
序列中最后一个单词是 endWord 。
每次转换只能改变一个字母。
转换过程中的中间单词必须是字典 wordList 中的单词。
给你两个单词 beginWord 和 endWord 和一个字典 wordList ，找到从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0。
"""

from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d
            
        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited: # // 已经遍历的不再重复遍历
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i+1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:  
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0
        
        d = construct_dict(set(wordList))
        return bfs_words(beginWord, endWord, d)

    
    res = ladderLength("", "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    print(res)
