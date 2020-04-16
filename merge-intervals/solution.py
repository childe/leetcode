# -*- coding: utf-8 -*-

'''
https://leetcode-cn.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

'''


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        rst = [intervals[0]]
        for (x,y) in intervals[1:]:
            if x <= rst[-1][1]:
                rst[-1] = [rst[-1][0], max(y,rst[-1][1])]
            else:
                rst.append([x,y])
        return rst


def main():
    s = Solution()
    r = s.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    a = [[1, 6], [8, 10], [15, 18]]
    assert r == a

    r = s.merge([[1, 4], [4, 5]])
    a = [[1, 5]]
    assert r == a

    r = s.merge([[1, 4], [0, 4]])
    a = [[0, 4]]
    assert r == a

    r = s.merge([[1, 4], [2, 3]])
    a = [[1, 4]]
    assert r == a


if __name__ == '__main__':
    main()
