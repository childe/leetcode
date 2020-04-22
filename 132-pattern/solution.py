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


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def buildBinTree(self, nums):
        root = Node(nums[0])
        for n in nums[1:]:
            node = root
            while node:
                if n <= node.val:
                    if node.left:
                        node = node.left
                    else:
                        node.left = Node(n)
                        break
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = Node(n)
                        break
        return root

    def find132patternFromBinTree(self, root):
        if root is None:
            return False
        if self.find132patternFromBinTree(root.left):
            return True
        if self.find132patternFromBinTree(root.right):
            return True
        r = root.right
        if r is not None and r.left is not None:
            return True
        return False

    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        root = self.buildBinTree(nums)

        return self.find132patternFromBinTree(root)


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
