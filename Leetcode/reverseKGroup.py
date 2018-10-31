"""
    比较难放弃吧
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k <= 1:
            return head
        h = ListNode(-1)
        h.next = head
        pre = h
        while pre:
            pre = self.reverseNextK(pre, k)
        return h.next

    def reverseNextK(self, head, k):
        # 检查是否有k个节点
        pre = head
        for i in range(k):
            if not pre.next:
                return None
            pre = pre.next

        node = head.next   # 最后的节点
        pre = head
        curr = head.next
        # 翻转
        for i in range(k):
            nextNode = curr.next
            curr.next = pre
            pre = curr
            curr = nextNode
        # 头尾连接
        node.next = curr
        head.next = pre
        return node