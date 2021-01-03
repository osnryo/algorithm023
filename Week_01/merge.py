# 88. 合并两个有序数组
# 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if 0 == n:
            pass
        elif 0 == m:
            nums1[:n] = nums2[:n]
        else:
            a, b = m-1, n-1
            k = m+n-1
            while (a>=0) and (b>=0):
                if nums1[a]<=nums2[b]: #  nums1 的元素尽量少动
                    nums1[k] = nums2[b]
                    k -= 1
                    b -= 1
                else:
                    nums1[k] = nums1[a]
                    k -= 1
                    a -= 1
            if (a>=0):
                pass
            if (b>=0):
                nums1[k-b:k+1] = nums2[:b+1]  # 必然有 k-b == 0，因为剩下的是最小的，必然是copy到最前面 


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]