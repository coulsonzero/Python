# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
    def mergeTwoLists(self, l1, l2):
        dummyHead = ListNode(0)
        prev = dummyHead
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        if l1 != None:
            prev.next = l1
        if l2 != None:
            prev.next = l2
        return dummyHead.next
