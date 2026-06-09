# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low , high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            if node.left:
                left = node.left
                if left.val >= node.val:
                    return False
            if node.right:
                right = node.right
                if right.val <= node.val:
                    return False        
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        return dfs(root, float('-inf'), float('inf'))
        