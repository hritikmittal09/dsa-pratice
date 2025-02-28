# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right



class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        if not preorder or not postorder:
            return None
    
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root

    # Find the left child in postorder
        left_root_index = postorder.index(preorder[1])

    # Recursively construct left and right subtrees
        root.left = self.constructFromPrePost(preorder[1:left_root_index+2], postorder[:left_root_index+1])
        root.right =self. constructFromPrePost(preorder[left_root_index+2:], postorder[left_root_index+1:-1])

        return root




        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        



        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        