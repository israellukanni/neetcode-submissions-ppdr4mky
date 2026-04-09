# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        res = []
        q = collections.deque([root])

        while q:
            right = None
            qlen = len(q)
            for i in range(qlen):
                curr = q.popleft()
                if curr:
                    right = curr
                    q.append(curr.left)
                    q.append(curr.right)
            if right:
                res.append(right.val)
        return res


