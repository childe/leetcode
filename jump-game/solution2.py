# -*- coding: utf-8 -*-

'''
https://leetcode-cn.com/problems/jump-game/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.


思路:
从后往前一个个遍历, 设置当前位是 True 还是 False. True 代表从当前能到.
最后返回 nums[0]

那如果确定 True 还是 False 呢?  我们记录最左边的 True 是哪一个, 如果当前的数字可以跳过这个 True, 它也是 True
'''


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        most_right = 0
        for i, n in enumerate(nums):
            if most_right < i:
                return False
            most_right = max(most_right, i+n)
        return most_right >= len(nums)-1


def main():
    s = Solution()

    assert s.canJump([2, 3, 1, 1, 4]) == True
    assert s.canJump([3, 2, 1, 0, 4]) == False


if __name__ == '__main__':
    main()
