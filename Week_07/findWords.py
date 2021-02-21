"""
212. 单词搜索 II
给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
"""


class Solution:
   def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True

        # (i,j)当前坐标，node当前trie树结点，pre前面的字符串，visited已访问坐标
        def search(i, j, node, pre, visited): 
            if '#' in node: 
                res.add(pre)
            for (di, dj) in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                _i, _j = i+di, j+dj
                  # 可继续搜索
                if -1 < _i < h and -1 < _j < w and board[_i][_j] in node and (_i, _j) not in visited:
                    # dfs搜索
                    search(_i, _j, node[board[_i][_j]], pre+board[_i][_j], visited | {(_i, _j)}) 

        res, h, w = set(), len(board), len(board[0])
        for i in range(h):
            for j in range(w):
                # 可继续搜索
                if board[i][j] in trie:  
                    # dfs搜索
                    search(i, j, trie[board[i][j]], board[i][j], {(i, j)})  
        return list(res)
