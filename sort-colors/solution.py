# -*- coding: utf-8 -*-

'''
https://leetcode-cn.com/problems/sort-colors/

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

'''


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        a, b, c = 0, 0, 0

        for c, n in enumerate(nums):
            # print(a, b, c, n, nums)
            if n == 0:
                if a == b: # 目前还没有1
                    # swap(c,a)
                    nums[c], nums[a] = nums[a], nums[c]
                    a += 1
                    b = a
                else:
                    # swap(c,a)
                    nums[c], nums[a] = nums[a], nums[c]
                    a += 1
                    nums[b], nums[c] = nums[c], nums[b]
                    b += 1
            elif n == 1:
                # swap(c, b)
                nums[b], nums[c] = nums[c], nums[b]
                b += 1
            # print('\t', a, b, c, n, nums)

        # print()


def main():
    s = Solution()
    import random
    nums = [0, 0, 0, 0, 0, 0, 2, 1, 0]
    s.sortColors(nums)
    print(nums)


    nums = [0, 0, 0, 0, 0, 0, 2, 1, 0, 2, 0, 2, 2, 0, 2]
    for i in range(len(nums)):
        input_value = nums[:i+1]
        s.sortColors(input_value)
        print(input_value)

    for _ in range(100):
        nums = [random.randint(0, 2) for _ in range(15)]
        output = sorted(nums)
        print(nums, output)
        s.sortColors(nums)
        print(nums, output)
        assert(nums == output)

    return

    nums = [0, 2, 2, 2, 0, 2, 1, 1]
    output = [0, 0, 1, 1, 2, 2, 2, 2]
    s.sortColors(nums)
    assert(nums == output)

    nums = [1, 0]
    output = [0, 1]
    s.sortColors(nums)
    assert(nums == output)

    nums = [1, 2, 1]
    output = [1, 1, 2]
    s.sortColors(nums)
    assert(nums == output)

    nums = [1, 1, 2]
    output = [1, 1, 2]
    s.sortColors(nums)
    assert(nums == output)

    nums = [1, 2]
    output = [1, 2]
    s.sortColors(nums)
    assert(nums == output)

    nums = [0, 1]
    output = [0, 1]
    s.sortColors(nums)
    assert(nums == output)

    nums = [2, 0, 2, 1, 1, 0]
    output = [0, 0, 1, 1, 2, 2]
    s.sortColors(nums)
    assert(nums == output)

    nums = []
    output = []
    s.sortColors(nums)
    assert(nums == output)

    nums = [2, 2]
    output = [2, 2]
    s.sortColors(nums)
    assert(nums == output)

    nums = [0, 2, 2]
    output = [0, 2, 2]
    s.sortColors(nums)
    assert(nums == output)

    nums = [0, 0, 2, 2]
    output = [0, 0, 2, 2]
    s.sortColors(nums)
    assert(nums == output)


if __name__ == '__main__':
    main()
