# 两数相加
"""
    给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，
    它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
    你可以假设除了数字 0 之外，这两个数字都不会以零开头。
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        输入的两个链表非空
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = node = ListNode('#')     # 输出的链表
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            carry, rem = divmod(carry+val1+val2, 10)
            # 连接输出数组的节点
            node.next = ListNode(rem)
            node = node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # 如果还有进位，加在下一个节点
        if carry:
            node.next = ListNode(carry)
        return head.next

if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(9)
    result = Solution().addTwoNumbers(a, b)

    # 1307
    print(result.val, result.next.val, result.next.next.val, result.next.next.next.val)
