"""
105. 从前序与中序遍历序列构造二叉树
根据一棵树的前序遍历与中序遍历构造二叉树。
"""

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 终止条件
        if not (preorder and inorder): return
        # 前序遍历第一个值为根节点
        root = TreeNode(preorder[0])
        # 因为没有重复元素，所以可以直接根据值来查找根节点在中序遍历中的位置
        mid = inorder.index(preorder[0])
        # 构建左子树
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # 构建右子树
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root


def buildTree(self, preorder, inorder):
    def build(stop):
        if inorder and inorder[-1] != stop:
            root = TreeNode(preorder.pop()) # 前序第一个节点做为根
            root.left = build(root.val)  # root.val：在中序中找到前序第一个节点的位置
            inorder.pop()
            root.right = build(stop)
            return root
    preorder.reverse()
    inorder.reverse()
    return build(None)