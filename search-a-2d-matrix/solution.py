# -*- coding: utf-8 -*-

'''
https://leetcode-cn.com/problems/search-a-2d-matrix/


Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        matrix = [row for row in matrix if row]
        col_one = [row[0] for row in matrix]
        print(col_one)
        row_x = self.binSearch(col_one, target, 0, len(col_one)-1)
        print("row_x", row_x)
        if row_x is None:
            return False
        for i in range(1+row_x):
            m = self.binSearch(matrix[i], target, 0, len(matrix[i])-1)
            print('m', m)
            if matrix[i][m] == target:
                return True
        return False

    def binSearch(self, nums, target, s, e):
        '''
        返回 <= target 的 index
        '''
        print(nums, target, s, e)
        if not nums:
            return None
        if s == e:
            return s
        if s > e:
            return None
        m = (s+e+1)//2
        if nums[m] == target:
            return m
        if nums[m] < target:
            return self.binSearch(nums, target, m, e)
        return self.binSearch(nums, target, s, m-1)


def main():
    s = Solution()

    # m = s.binSearch([10, 11, 16, 20], 13, 0, 3)
    # print(m)

    matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
    ]
    target = 3
    ans = s.searchMatrix(matrix, target)
    print(ans)
    assert(ans is True)

    matrix = [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
        ]
    target = 13
    ans = s.searchMatrix(matrix, target)
    print(ans)
    assert(ans is False)

    matrix = [ [] ]
    target = 1
    ans = s.searchMatrix(matrix, target)
    print(ans)
    assert(ans is False)



if __name__ == '__main__':
    main()
