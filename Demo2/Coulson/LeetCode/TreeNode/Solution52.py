# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
前序遍历： 根左右
中序遍历： 递增节点序列
后序遍历： 子节点-节点-根节点
层序遍历： 自上到下，自左到右

lc 二叉树的前序遍历(先根节点，再层序左节点，再层序右各个节点)
                   F
                 /   \
                B     G
               / \     \
              A   D     I
                 / \    /
                C   E  H
                
输出： F B A D C E G I H 

输入：root = [1,null,2,3]
输出：[1,2,3]
'''
class Solution:
    def __init__(self):
        self.root = TreeNode()

    def add(self, val): pass
    '''
    执行用时：28 ms, 在所有 Python3 提交中击败了98.98%的用户
    '''
    def preorderTraversal(self, root: TreeNode):
        def preorder(root):
            if root == None:
                return
            a.append(root.val)  #前
            preorder(root.left)
            preorder(root.right)
        a = []
        preorder(root)
        return a

    def inOrderTraversal(self, root: TreeNode):
        # 实现中序遍历方法
        def inorder(root: TreeNode):
            if root == None:
                return
            inorder(root.left)
            a.append(root.val)
            inorder(root.right)

        # 创建数组队列(存储返回结点)
        a = list()
        inorder(root)
        return a

    def postorderTraversal(self, root: TreeNode):
        # 实现中序遍历方法
        def postorder(root: TreeNode):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            a.append(root.val)

        # 创建数组队列(存储返回结点)
        a = list()
        postorder(root)
        return a

    def levelOrder(self, root: TreeNode):
        if not root: return []  # 基本情况直接返回
        queue = [root]  # 主队列
        res = []  # 初始值

        while queue:
            temp = []  # 临时队列
            res.append([i.val for i in queue])
            for item in queue:  # 把下一层的每个元素都放到队列
                if item.left: temp.append(item.left)
                if item.right: temp.append(item.right)
            queue = temp  # 把临时队列赋值给主队列
        return res