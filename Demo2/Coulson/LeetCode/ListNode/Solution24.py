
'''
lc 21. 合并两个有序链表

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

思路：新建指针，依次比较两个链表值大小，并移动指针
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    '''
        dummyHead = ListNode(0)
        prev = dummyHead
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next =l2
                l2 = l2.next
            prev = prev.next

        if l1 !=None:
            prev.next = l1
        if l2 != None: 
            prev.next = l2
        return dummyHead.next
    '''
if __name__ == '__main__':
    t = Solution()
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    print(t.mergeTwoLists(l1, l2))