# -*- coding:utf-8 -*-

""" 
@author: 付登龙
@file: solution.py
@time: 2019/02/16 11:31 PM
"""
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(0)
        self.merge(head, lists)
        return head.next

    def merge(self, result: ListNode, lists: List[ListNode]):
        m = None
        for index in range(len(lists)):
            if m is None and lists[index] is not None:
                m = index
                continue
            if lists[index] is not None and lists[index].val < lists[m].val:
                m = index
        if m is not None:
            result.next = ListNode(lists[m].val)
            result = result.next
            lists[m] = lists[m].next
            self.merge(result, lists)


if __name__ == '__main__':
    pass
