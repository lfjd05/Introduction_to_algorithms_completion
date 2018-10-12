"""
    给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode  链表节点
        :type n: int
        :rtype: ListNode
        """
        # 读取链表
        list0 = []
        count = 0
        while head:
            list0.append(head)
            # 头结点定义
            head = head.next
            # 表长度
            count += 1

        if count == 1:
            return None
        if list0[-n].next is None:   # 如果该节点是最后一个
            list0[-n-1].next = None
            return list0[0]
        else:   # 与其说是删除不如说像剪切操作
            list0[-n].val = list0[-n].next.val   # 后继的数值覆盖给原数值
            list0[-n].next = list0[-n].next.next  #
        return list0[0]


# print(Solution().removeNthFromEnd([1,2,3,4,5],2))
