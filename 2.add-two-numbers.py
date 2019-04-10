#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (30.87%)
# Total Accepted:    822.2K
# Total Submissions: 2.7M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Example:
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getNum(self, l, s, mult):
        s = s + l.val * mult
        if l.next != None:
            s = self.getNum(l.next, s, mult * 10)
        return s

    def reverseToList(self, num, l):
        if l == "":
            l = ListNode(num % 10)
            num = num // 10
        if num > 0:
            l.next = ListNode(num % 10)
            l.next = self.reverseToList(num // 10, l.next)
        return l

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.getNum(l1, 0, 1)
        num2 = self.getNum(l2, 0, 1)
        l = ""
        return self.reverseToList(num1 + num2, l)
