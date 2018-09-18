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


class LinkList:
    def __init__(self):
        """
            链表变量初始化
        """
        self.length = 0
        self.head = None

    def is_empty(self):
        # 判断是否空
        return self.length == 0

    def append(self, insert_node):
        if isinstance(insert_node, ListNode):   # 判断是否节点类型
            pass
        if self.is_empty():
            self.head = insert_node
        else:
            node = self.head    # 临时节点先放起点
            while node.next:   # 如果还没到尾部
                node = node.next
            node.next = insert_node
        self.length += 1


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        输入的两个链表非空
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp = ListNode(0)
        res = tmp
        flag = 0
        while l1 or l2:
            tmpsum = 0
            if l1:
                tmpsum = l1.val
                l1 = l1.next
            if l2:
                tmpsum += l2.val    # 节点求和
                l2 = l2.next
            tmpres = ((tmpsum + flag) % 10)   # 带进位的求和，过滤掉大于9的部分
            flag = ((tmpsum + flag) // 10)
            res.next = ListNode(tmpres)
            res = res.next
        if flag:
            res.next = ListNode(1)
        res = tmp.next
        del tmp
        print(res.val)
        return res


# l1_data = [2, 4, 3]
# l2_data = [5, 6, 4]
#
# L1 = LinkList()
# for i in l1_data:
#     L1.append(i)
# data = [(2, 5), (4, 6), (3, 4)]
# a = Solution()
for i, j in data:
    a.addTwoNumbers(ListNode(i), ListNode(j))
