# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        h = ListNode(-1)  # 头结点
        h.next = head
        pre = h
        while pre.next is not None and pre.next.next is not None:
            node1=pre.next    # 前驱结点赋值给1节点
            node2=node1.next  # 2节点赋值
            lat=node2.next    # 后继结点赋值

            pre.next = node2  # 2节点交换到1位置
            node2.next = node1  # 2节点的next 改指向
            node1.next = lat   # 1节点的新指向是后继
            pre = node1  # 前驱向前移动
        return h.next
