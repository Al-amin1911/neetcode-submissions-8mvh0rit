# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        
        # 1. The first element in preorder is always the root of the current subtree
        root = TreeNode(preorder[0]) 

        # 2. Find where this root splits the inorder list
        mid = inorder.index(root.val)

        # 3. Slice the arrays and recursively build the left and right subtrees
        # Left subtree inorder elements are from 0 to mid
        # Left subtree preorder elements are the next 'mid' elements after the root
        root.left = self.buildTree(preorder[1 : mid+1], inorder[:mid])

        # Right subtree takes whatever is left over in both arrays
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
        


        


        
        