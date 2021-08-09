# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
lc 206. 反转链表
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

执行用时：40 ms, 在所有 Python3 提交中击败了84.54%的用户
'''

class Solution:
    def reverseList(self, head):
        pre = None  # Java为null
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre