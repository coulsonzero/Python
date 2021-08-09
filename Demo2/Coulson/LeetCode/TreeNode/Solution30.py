# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
lc 二叉树的最大深度

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。

输入：[3,9,20,null,null,15,7]
输出：3
    3
   / \
  9  20
    /  \
   15   7
'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 深度优先递归
        return 0 if not root else 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
    '''
        if(root == None):
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + ( left if left >= right else right)
    '''