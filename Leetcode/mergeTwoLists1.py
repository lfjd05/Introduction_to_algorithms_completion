"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 最简单情况
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        head = ListNode(0)
        pre = head   # 当前操作指针

        while l1 and l2:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next  # 原来的链表删除l1
            else:
                pre.next = l2
                l2 = l2.next
            # 移动pre指针
            pre = pre.next
        # 添加剩余元素
        if l1:
            pre.next = l1
        if l2:
            pre.next = l2
        return head.next
