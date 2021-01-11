# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(root)
            nonlocal res
            if not root:
                return

            res.append(root.val)  #先将根节点值加入结果
            dfs(root.left)  #左
            dfs(root.right) #右

        dfs(root)
        return res


class Solution:
    def preorderTraversal2(self, root: TreeNode) -> List[int]:
        if root is None: 
            return []

        stack, res = [root, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                res.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None: 
                    stack.append(root.left)
        return res