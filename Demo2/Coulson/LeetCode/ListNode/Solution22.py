'''
lc 删除链表的倒数第N个节点
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
输入：head = [1], n = 1

思路：快慢指针，都从头节点开始，fast指针先移动n步，然后快慢指针同时移动，使慢指针指向要删除的节点之前，再删除这个要删除的节点即可
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        # 让快慢指针都从head头节点开始
        dummy = ListNode(0, head)  # 关键
        fast = head
        slow = dummy
        # 快指针先移动n+1步
        for i in range(n):
            fast = fast.next
        # 快慢指针同时移动，最后快指针指向None，慢指针位于要删除的节点之前
        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
