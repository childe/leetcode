# -*- coding: utf-8 -*-

"""
https://leetcode.cn/problems/rotate-array/description/

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1
0 <= k <= 10^5
 

Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        magic = 1 << 32
        for i in range(n):
            nums[i] += magic

        pointer = -1
        for _ in range(k):
            pointer = (pointer + 1) % n
            tmp = nums[pointer]
            while True:
                next_pointer = (pointer + k) % n
                if nums[next_pointer] < 0:
                    break
                nums[next_pointer], tmp = -tmp, nums[next_pointer]
                pointer = next_pointer

        for i in range(n):
            if nums[i] < 0:
                nums[i] = -nums[i] - magic
            else:
                nums[i] = nums[i] - magic

        print(nums)


def main():
    solution = Solution()
    solution.rotate([1, 2, 3, 4, 5, 6, 7], 3)
    solution.rotate(nums=[-1, -100, 3, 99], k=2)
    solution.rotate(nums=[1], k=0)
    solution.rotate(nums=[1], k=2)


if __name__ == "__main__":
    main()
