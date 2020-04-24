# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/132-pattern/

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.

Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        candidates = [[nums[0]]]
        for n in nums:
            # print(candidates)
            if n < candidates[-1][0]:
                candidates.append([n])
                continue
            if n == candidates[-1][0]:
                continue
            for c in candidates:
                if len(c) == 2:
                    if c[0] < n < c[1]:
                        return True
                    if n > c[1]:
                        c[1] = n
                else:
                    if n > c[0]:
                        c.append(n)
                    else:
                        c[0] = n

            # if append is False and [n] not in candidates:
                # candidates.append([n])
        return False


def main():
    s = Solution()

    Input = [1, 2, 3, 4]
    Output = False
    ans = s.find132pattern(Input)
    print(ans)
    assert ans == Output

    Input = [3, 1, 4, 2]
    Output = True
    ans = s.find132pattern(Input)
    print(ans)
    assert ans == Output

    Input = [-1, 3, 2, 0]
    Output = True
    ans = s.find132pattern(Input)
    print(ans)
    assert ans == Output


if __name__ == '__main__':
    main()
