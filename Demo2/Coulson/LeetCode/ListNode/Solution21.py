

'''
lc 删除链表中的节点
输入：head = [4,5,1,9], node = 5
输出：[4,1,9]

解释：从链表里删除一个节点 node 的最常见方法是修改之前节点的 next 指针，使其指向之后的节点。
4-> 5 ->9
4------>9
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #把要删除结点的下一个结点的值赋给要删除的结点
        node.val = node.next.val
        #然后删除下一个结点
        node.next = node.next.next