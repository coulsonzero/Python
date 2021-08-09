### TreeNode

#### 二叉树结构
```
        3
       / \
      9  20
     / \ / \
   -1 -1 5  7

[
 [3],
 [9,20],
 [-1,-1,5,7]
]
```

**代码结构**
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

#### 遍历方法

* 前序遍历： 根左右
* 中序遍历： 递增节点序列
* 后序遍历： 子节点-节点-根节点
* 层序遍历： 自上到下，自左到右

#### 前序遍历
```python
# 前序遍历：输出列表
def preorderTraversal(self, root):
    def preOrder(root):
        if root == None:
            return
        a.append(root.val)
        preOrder(root.left)
        preOrder(root.right)
    a = []
    preOrder(root)
    return a
```

#### 中序遍历
```python
def inOrderTraversal(self, root):
        # 实现中序遍历方法
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            a.append(root.val)
            inorder(root.right)
        # 创建数组队列(存储返回结点)
        a = list()
        inorder(root)
        return a
```
#### 中序遍历    
```python
def postorderTraversal(self, root):
        # 实现中序遍历方法
        def postorder(root):
            if not root:
                return
            postorder(root.left)
            postorder(root.right)
            a.append(root.val)

        # 创建数组队列(存储返回结点)
        a = list()
        postorder(root)
        return a

    
```
#### 层序遍历(自上而下，自左而右)
```python
def levelOrder(self, root):
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
```
    
