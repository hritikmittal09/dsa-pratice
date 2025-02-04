class Solution(object):
    def invertTree(self, root):
        if root is None:
            return None
        l = self. invertTree(root.left)
        r = self. invertTree(root.right)
        root.left = r
        root.right = l
        return root