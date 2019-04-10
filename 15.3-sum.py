#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (23.72%)
# Total Accepted:    516.8K
# Total Submissions: 2.2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
#
#
#


class Solution:
    def threeSum(self, nums):
        zeroList = [i for i in nums if i == 0]
        posList = [i for i in nums if i > 0]
        negList = [i for i in nums if i < 0]
        posList.sort()
        negList.sort()
        posSet = set(posList)
        negSet = set(negList)
        ans = set()
        # all zero
        if len(zeroList) > 2:
            ans.add((0, 0, 0))
        # neg zero pos
        if len(zeroList) > 0:
            for negNum in negList:
                if - negNum in posSet:
                    ans.add((negNum, 0, -negNum))
        # neg neg pos
        negLen = len(negList)
        for neg1 in range(negLen):
            for neg2 in range(neg1 + 1, negLen):
                negSum = negList[neg1] + negList[neg2]
                if -negSum in posSet:
                    ans.add((negList[neg1], negList[neg2], -negSum))
        # neg pos pos
        posLen = len(posList)
        for pos1 in range(posLen):
            for pos2 in range(pos1 + 1, posLen):
                posSum = posList[pos1] + posList[pos2]
                if - posSum in negSet:
                    ans.add((posList[pos1], posList[pos2], -posSum))
        return list(ans)
