# -*- coding: utf-8 -*-

'''
https://leetcode-cn.com/problems/diagonal-traverse/

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:

 

Note:

The total number of elements of the given matrix will not exceed 10,000.

'''


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        i, j, rst = 0, 0, []
        d = 1
        while True:
            # print(i, j, matrix[i][j], rst)
            rst.append(matrix[i][j])
            if i == len(matrix)-1 and j == len(matrix[-1])-1:
                break

            if d == 1:
                if j == len(matrix[i])-1:
                    i += 1
                    d = -d
                    continue
                if i == 0:
                    j += 1
                    d = -d
                    continue
                i -= 1
                j += 1
            else:
                if i == len(matrix) - 1:
                    j += 1
                    d = -d
                    continue
                if j == 0:
                    i += 1
                    d = -d
                    continue
                i += 1
                j -= 1

        return rst


def main():
    s = Solution()

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    output = [1, 2, 4, 7, 5, 3, 6, 8, 9]
    a = s.findDiagonalOrder(matrix)
    print(a)
    assert(a == output)


if __name__ == '__main__':
    main()
