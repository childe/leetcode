#!/usr/bin/env python3
"""
https://leetcode.cn/problems/sliding-window-maximum/
"""


class MonotonicQueue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        while self.queue and self.queue[-1] < item:
            self.queue.pop()
        self.queue.append(item)

    def pop(self):
        r = self.queue[0]
        self.queue = self.queue[1:]
        return r

    def top(self):
        return self.queue[0]


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = []
        q = MonotonicQueue()
        for i in range(k):
            q.push(nums[i])
        # print(nums[:k], q.queue)
        ans = [q.queue[0]]
        for i in range(k, len(nums)):
            # print(nums[i : i + k], q.queue)
            if nums[i - k] == q.top():
                q.pop()
            q.push(nums[i])
            ans.append(q.queue[0])

        return ans


import unittest


class TestSolution(unittest.TestCase):
    def test_maxSlidingWindow(self):
        solution = Solution()
        self.assertEqual(solution.maxSlidingWindow([9, 8, 9, 8], 3), [9, 9])
        self.assertEqual(solution.maxSlidingWindow([1, -1], 1), [1, -1])
        self.assertEqual(
            solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3), [3, 3, 5, 5, 6, 7]
        )
        self.assertEqual(solution.maxSlidingWindow([1], 1), [1])
        self.assertEqual(solution.maxSlidingWindow([9, 11], 2), [11])
        self.assertEqual(solution.maxSlidingWindow([4, -2], 2), [4])
        self.assertEqual(solution.maxSlidingWindow([1, 3, 1, 2, 0, 5], 3), [3, 3, 2, 5])


if __name__ == "__main__":
    unittest.main()
