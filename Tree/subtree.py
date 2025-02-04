# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isIdentical(self, root1, root2):
        """Checks if two trees are identical"""
        if not root1 and not root2:
            return True  # Both are None
        if not root1 or not root2:
            return False  # One is None, the other isn't
        return (
            root1.val == root2.val and
            self.isIdentical(root1.left, root2.left) and
            self.isIdentical(root1.right, root2.right)
        )
    def isSubtree(self, root, subRoot):
        if not root:
            return False  # If main tree is empty, subRoot can't be a subtree
        if self.isIdentical(root, subRoot):
            return True  # If identical, return True
        # Check in left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        