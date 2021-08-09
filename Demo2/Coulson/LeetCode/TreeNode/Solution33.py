# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
lc 102. 二叉树的层序遍历
二叉树：[3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
   
输出：
[
  [3],
  [9,20],
  [15,7]
]
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        #跟结点入queue
        queue = [root]
        res = []
        while queue:
            res.append([node.val for node in queue])
            #存储当前层的子节点列表
            ll = []
            #对当前层的每个节点遍历
            for node in queue:
                #如果左子节点存在，入队列
                if node.left:
                    ll.append(node.left)
                #如果右子节点存在，入队列
                if node.right:
                    ll.append(node.right)
            #后把queue更新成下一层的结点，继续遍历下一层
            queue = ll
        return res
    
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        nodes = []
        self.levelNext(root,0,nodes)
        return nodes
    def levelNext(self,root,depth,nodes):
        if root == None:
            return
        while len(nodes)-1 < depth:
            nodes.append([])

        nodes[depth].append(root.val)
        self.levelNext(root.left,depth+1,nodes)
        self.levelNext(root.right,depth+1,nodes)
'''