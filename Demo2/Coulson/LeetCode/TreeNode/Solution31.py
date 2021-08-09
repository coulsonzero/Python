# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
lc 98. 验证二叉搜索树
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。


节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树

执行用时：48 ms, 在所有 Python3 提交中击败了91.02%的用户
'''
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.DFS(root)
    def DFS(self, root, left=None, right=None):
        if not root:
            return True
        if (left and left.val >= root.val) or (right and right.val <= root.val):
            return False
        return self.DFS(root.left, left, root) and self.DFS(root.right, root, right)
'''
执行用时：48 ms, 在所有 Python3 提交中击败了91.02%的用户
'''