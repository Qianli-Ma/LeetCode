#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (46.53%)
# Total Accepted:    547.4K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None
        elif l1 is None:
            return l2
        elif l2 is None:
            return l1
        tempNode = curNode = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curNode.next = l1
                l1 = l1.next
            else:
                curNode.next = l2
                l2 = l2.next
            curNode = curNode.next
        if l1 == None:
            while l2:
                curNode.next = l2
                l2 = l2.next
                curNode = curNode.next
        elif l2 == None:
            while l1:
                curNode.next = l1
                l1 = l1.next
                curNode = curNode.next
        return tempNode.next
