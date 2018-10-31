# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/

A sequence X_1, X_2, ..., X_n is fibonacci-like if:

n >= 3
X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
Given a strictly increasing array A of positive integers forming a sequence, find the length of the longest fibonacci-like subsequence of A.  If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)



Example 1:
Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].

Example 2:
Input: [1,3,7,11,12,14,18]
Output: 3
Explanation:
The longest subsequence that is fibonacci-like:
[1,11,12], [3,11,14] or [7,11,18].


Note:

3 <= A.length <= 1000
1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
(The time limit has been reduced by 50% for submissions in Java, C, and C++.)
"""


class Solution(object):
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        allN = set(A)
        arr = []  # (length, last_num, num_before_last_num)
        for i, n in enumerate(A):
            arr.append(dict())

        # for i, a in enumerate(arr):
            # print i, a

        r = 0
        for i, n in enumerate(A):
            # print i, n
            for j in range(i):
                jn = A[j]
                d = arr[j]
                # print '\t', j, A[j], len(d), d
                if n - jn < jn and n - jn in d:
                    arr[i][jn] = d[n-jn]+1
                else:
                    if n-jn < jn and n - jn in allN:
                        arr[i][jn] = 3

                if r < arr[i].get(jn, 0):
                    r = arr[i][jn]

        # for i, a in enumerate(arr):
            # print i, a

        return r if r > 2 else 0


def main():
    s = Solution()
    print s.lenLongestFibSubseq(range(1, 1000))
    print s.lenLongestFibSubseq(range(1, 9))
    print s.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18])
    print s.lenLongestFibSubseq([2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50])

    for line in open('input.txt').readlines():
        line = line.strip()
        print s.lenLongestFibSubseq(eval(line))


if __name__ == '__main__':
    main()
