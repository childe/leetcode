# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/flatten-nested-list-iterator/description/

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].

Example 2:
Given the list [1,[4,[6]]],

By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedIterator(object):
    def __push_to_integers(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        """
        for ni in nestedList:
            if ni.isInteger():
                self.integers.append(ni.getInteger())
            else:
                self.__push_to_integers(ni.getList())

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.index = 0
        self.integers = []
        for ni in nestedList:
            if ni.isInteger():
                self.integers.append(ni.getInteger())
            else:
                self.__push_to_integers(ni.getList())
        self.size = len(self.integers)

    def next(self):
        """
        :rtype: int
        """
        r = self.integers[self.index]
        self.index += 1
        return r

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.size > self.index


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
