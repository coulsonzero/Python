class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.root = TreeNode()

    def add(self, val):
        node = TreeNode(val)
        if self.root.val == 0:
            self.root = node
        else:
            myqueue = []
            treeNode = self.root
            myqueue.append(treeNode)
            while myqueue:
                treeNode = myqueue.pop(0)
                if not treeNode.left:
                    treeNode.left = node
                    return
                elif not treeNode.right:
                    treeNode.right = node
                    return
                else:
                    myqueue.append(treeNode.left)
                    myqueue.append(treeNode.right)
    # 前序遍历
    def preOrder(self, root):
        if root == None:
            return
        print(root.val)
        self.preOrder(root.left)
        self.preOrder(root.right)

    # 中序遍历
    def inOrder(self, node: TreeNode):
        if node == None:
            return
        self.inOrder(node.left)
        print(node.val)
        self.inOrder(node.right)

    # 后序遍历
    def postorder(self, root: TreeNode):
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)



    # 前序遍历：输出列表
    def preorderTraversal(self, root: TreeNode):
        def preOrder(root):
            if root == None:
                return
            a.append(root.val)
            preOrder(root.left)
            preOrder(root.right)
        a = []
        preOrder(root)
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

    # 层序遍历(自上而下，自左而右)
    '''
        3
       / \
      9  20
        /  \
       15   7
    [
      [3],
      [9,20],
      [15,7]
    ]
    '''
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






if __name__ == '__main__':
    roots = [3, 5, 7, -1, -1, 2, 6]
    tree = Solution()
    for i in roots:
        if i > 0:
            tree.add(i)
    print(tree.levelOrder(tree.root))

'''
       3
     /   \
    5     7
   / \   / \
 -1  -1 2   6

'''