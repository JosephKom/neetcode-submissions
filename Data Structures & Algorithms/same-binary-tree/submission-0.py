# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.BFS(p, q)
    
    def BFS(self, p, q):
        if p is None and q is None:
            return True
        elif p is None:
            return False
        elif q is None:
            return False
        elif p.val != q.val:
            return False

        return self.BFS(p.left, q.left) and self.BFS(p.right, q.right)
