# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        left_to_right = []
        s = []
        for i, n in enumerate(heights):
            while s:
                if s[-1][0] >= n:
                    s.pop()
                else:
                    left_to_right.append((n, s[-1][1]))
                    s.append((n, i))
                    break
            if not s:
                s.append((n, i))
                left_to_right.append((n, -1))

        # print(left_to_right)

        right_to_left = []
        s = []
        for i in range(len(heights)-1, -1, -1):
            n = heights[i]
            while s:
                if s[-1][0] >= n:
                    s.pop()
                else:
                    right_to_left.insert(0, (n, s[-1][1]))
                    s.append((n, i))
                    break
            if not s:
                s.append((n, i))
                right_to_left.insert(0, (n, len(heights)))

        # print(right_to_left)

        return max([h * (right_to_left[i][1] - left_to_right[i][1]-1) for i, h in enumerate(heights)])


def main():
    s = Solution()
    ans = s.largestRectangleArea([2, 1, 5, 6, 2, 3])
    print(ans)
    assert ans == 10

    ans = s.largestRectangleArea([1, 1])
    print(ans)
    assert ans == 2


if __name__ == '__main__':
    main()
