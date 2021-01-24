"""
874. 模拟行走机器人
机器人在一个无限大小的 XY 网格平面上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令 commands ：

-2 ：向左转 90 度
-1 ：向右转 90 度
1 <= x <= 9 ：向前移动 x 个单位长度
在网格上有一些格子被视为障碍物 obstacles 。第 i 个障碍物位于网格点  obstacles[i] = (xi, yi) 。
机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续尝试进行该路线的其余部分。
返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。（即，如果距离为 5 ，则返回 25 ）
注意：
北表示 +Y 方向。
东表示 +X 方向。
南表示 -Y 方向。
西表示 -X 方向。
"""
class Solution:
    def robotSim(self, commands, obstacles):
        i = j = mx = d = 0
        move, obstacles = [(0, 1), (-1, 0), (0, -1), (1, 0), ], set(map(tuple, obstacles))
        for command in commands:
            if command == -2: d = (d + 1) % 4 # -1：向右转 90 度
            elif command == -1: d = (d - 1) % 4 # -2：向左转 90 度
            else: # 1 <= x <= 9：向前移动 x 个单位长度
                x, y = move[d]
                # 当前坐标不是障碍点，计算并与存储的最大欧式距离的平方做比较
                while command and (i + x, j + y) not in obstacles:
                    i += x
                    j += y
                    command -= 1
            mx = max(mx, i ** 2 + j ** 2)
        return mx