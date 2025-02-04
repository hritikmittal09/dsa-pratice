# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def slove (root,m):
    if root is None:
        return 0
    l = slove(root.left,m)
    r = slove(root.right,m)
    neecheVlaSum = l +r+ root.val
    chooseOne = max(l,r) + root.val
    chooseRoot = root.val
    m[0] = max(neecheVlaSum, chooseOne,chooseRoot,m[0])   
    return max(chooseRoot,chooseOne) 
class Solution(object):
    def maxPathSum(self, root):
        m = [float('-inf')]
        slove(root,m)
        return m[0]
        