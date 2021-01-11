# 429. N 叉树的层序遍历

class Solution:
    def levelOrder(self, root):
        if not root: return []
        queue = [root]
        res = []
        while queue:
            res.append(node.val for node in queue)
            queue = [child for node in queue for child in node.children]
        return res


from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None: return []
        res = []
        q = deque([(root,0)])
        while q:
            n,l = q.popleft()
            if len(res) < l +1:
                res.append([])
            for i in n.children:
                q.append((i,l+1))
            res[l].append(n.val)
        return res