"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # 存链表数据
        list1 = []
        list2 = []

        count = 0
        while l1:
            list1.append(l1)
            l1 = l1.next
            count += 1
        count = 0
        while l2:
            list2.append(l2)
            l2 = l2.next
            count += 1

        result = []
        while len(list1) > 0 and len(list2) > 0:
            if list1[0].val < list2[0].val:
                result.append(list1.pop(0))
            else:
                result.append(list2.pop(0))
        result += list1
        result += list2
        return result
