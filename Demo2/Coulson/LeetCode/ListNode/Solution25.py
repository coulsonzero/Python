'''
lc 回文链表

输入: 1->2->2->1
输出: true
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''
    思路：
    1. 复制后切片反转
        时间复杂度：
        空间复杂度
    2. 双指针
        pre
        None 1 -> 2 -> 4 -> 4 -> 2 -> 1 -> None
        fast
        slow
        pre

                      pre
        None 1 <- 2 <- 4 -> 4 -> 2 -> 1 -> None
                    prepre slow             fast
        a. 找到中间节点(fast=fast.next.next, slow=slow.next)
        b. 另一个指针反转中间节点之前的所有指针
        c. 从中间节点两个指针不断遍历
    '''
    def isPalindrome(self, head: ListNode) -> bool:
        if (head == None or head.next == None):  # 特殊情况
            return True
        slow = fast = pre = head
        prepre = None


        while (fast != None and fast.next != None):
            # 寻找中点的同时反转一半的链表,fast.next != null用于保证该链表是偶数个数的链表
            pre = slow
            slow = slow.next
            fast = fast.next.next
            # 反转链表
            pre.next = prepre
            prepre = pre
        # 元素个数为奇数的情况
        if (fast != None):
            slow = slow.next
        # 判断回文子串
        while (pre != None and slow != None):
            if (pre.val != slow.val):
                return False
            pre = pre.next
            slow = slow.next
        return True

    '''
    执行用时：624ms, 在所有Python3提交中击败了98.98%的用户
    内存消耗：32.3 MB, 在所有Python3提交中击败了99.64%的用户
    '''


    '''
        val = []
        while head:
            val.append(head.val)
            head = head.next
        return val == val[::-1]
    '''


