学习笔记

一、深度优先搜索和广度优先搜索
基于图的搜索

-----BFS-----
定义：“地毯式”层层推进的搜索策略，即先查找离起始顶点最近的，然后是次近的，依次往外搜索

三个重要的辅助变量 
1、visited：是用来记录已经被访问的顶点，用来避免顶点被重复访问。
2、queue：是一个队列，用来存储已经被访问、但相连的顶点还没有被访问的顶点
3、prev：用来记录搜索路径

复杂度：
1、时间复杂度:O(E)
2、空间复杂度:O(V)

-----DFS-----
深度优先搜索用的是回溯思想，适合用递归来实现。

复杂度：
1、时间复杂度:O(E)
2、空间复杂度:O(V)


二、二分查找
定义：
二分查找针对的是一个有序的数据集合，查找思想有点类似分治思想。每次都通过跟区间的中间元素对比，将待查找的区间缩小为之前的一半，直到找到要查找的元素，或者区间被缩小为 0。

时间复杂度：
O(logn)

容易出错的 3 个地方:
1、循环退出条件
2、mid 的取值
3、low 和 high 的更新

应用场景的局限：
1、二分查找依赖的是顺序表结构（数组）
2、针对有序数据
3、数据量太小不适合二分查找
4、数据量太大也不适合二分查找

二分查找的变形问题：
变体一：查找第一个值等于给定值的元素
变体二：查找最后一个值等于给定值的元素
变体三：查找第一个大于等于给定值的元素
变体四：查找最后一个小于等于给定值的元素

二分查找需要注意：
1、终止条件、
2、区间上下界更新方法、
3、返回值选择


三、贪心算法
定义：
它是一种算法思想，每次都选择最优解。
每一步都采取当下最优的解，从而希望结果是最优。

步骤：
1、当遇到限制值和期望值同时有的这类问题，要想到用贪心算法
2、尝试使用贪心算法解决
3、举几个例子验证贪心算法产生结果是否最优

缺陷：
贪心算法解决问题的思路，并不总能给出最优解

应用：
1、霍夫曼编码（Huffman Coding）（数据压缩）
2、Prim 和 Kruskal 最小生成树算法
3、Dijkstra 单源最短路径算法

适用场景有限，主要是知道设计基础算法。