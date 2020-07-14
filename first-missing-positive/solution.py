# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/first-missing-positive/

41. First Missing Positive
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3

Example 2:

Input: [3,4,-1,1]
Output: 2

Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1

        min_value, max_value, l = min(nums), max(nums), len(nums)
        if max_value <= 0:
            return 1

        for n in nums:
            # print(nums)
            if n < min_value:
                n -= min_value
            elif n > max_value:
                n -= 1 + max_value

            # print("n", n)

            if n <= 0:
                continue
            if n > l:
                continue
            idx_num = nums[n - 1]
            # print("idx_num", idx_num)

            # 已经改过一次了
            if idx_num < min_value or idx_num > max_value:
                continue

            if idx_num < 0:
                nums[n - 1] = min_value + idx_num
            else:
                nums[n - 1] = max_value + idx_num + 1

        # print(nums)
        for i, n in enumerate(nums):
            if n < min_value:
                continue
            if n > max_value:
                continue
            return i + 1
        return l + 1


def main():
    s = Solution()

    ans = s.firstMissingPositive([0, 1, 2])
    print(ans)
    assert ans == 3

    ans = s.firstMissingPositive([1, 1, 1])
    print(ans)
    assert ans == 2

    ans = s.firstMissingPositive([1, 2, 3])
    print(ans)
    assert ans == 4

    ans = s.firstMissingPositive([3, 2, 1])
    print(ans)
    assert ans == 4

    ans = s.firstMissingPositive([1, 2, 0])
    print(ans)
    assert ans == 3

    ans = s.firstMissingPositive([3, 4, -1, 1])
    print(ans)
    assert ans == 2

    ans = s.firstMissingPositive([7, 8, 9, 11, 12])
    print(ans)
    assert ans == 1


if __name__ == "__main__":
    main()
