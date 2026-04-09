# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        res = []
        que = collections.deque()
        que.append(root)
        

        while que:
            level = []
            for i in range(len(que)):
                curr = que.popleft()
                if curr: 
                    level.append(curr.val)
                    que.append(curr.left)
                    que.append(curr.right)
            if level:
                res.append(level)
        return res

        


        