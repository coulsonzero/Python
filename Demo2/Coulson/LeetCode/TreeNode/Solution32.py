# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
lc 对称二叉树

    1
   / \
  2   2
 / \ / \
3  4 4  3
True
'''
class Solution:
    # 递归
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return self.check(root.left,root.right)

    def check(self,left,right):
        if left == None and right == None:
            return True
        if left == None or right == None or left.val != right.val:
            return False
        return self.check(left.left, right.right) and self.check(left.right,right.left)
