"""
190. 颠倒二进制位
颠倒给定的 32 位无符号整数的二进制位。
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = (n >> 16) | (n << 16) & 0xffffffff
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8) & 0xffffffff
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4) & 0xffffffff
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2) & 0xffffffff
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1) & 0xffffffff
        return n