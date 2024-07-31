# -*- coding: utf-8 -*-


"""
https://leetcode-cn.com/problems/minimum-window-substring/

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""


from collections import deque


class Solution(object):
    def minWindow(self, s: str, t: str) -> str:
        # t 中每个字符的数量出现在滑动窗口中的数量。初始化时为负数。每出现一次就+1，等于0时表示t中的这个字符已经出现在滑动窗口中足够的次数。
        # 当所有字符的值都为0时，表示滑动窗口中的字符已经包含了t中的所有字符。
        char_nums = {}
        for c in t:
            char_nums[c] = char_nums.get(c, 0) - 1

        # 滑动窗口吧。里面包含了 t 中的字符，开始时数量可能不够，滑动过程中会增加
        queue = deque()

        def try_clean_queue():
            """
            尝试清理队列，如果最左边的字符数量多于t中出现的次数时，去掉。相当于窗口左边向右移动。
            """
            while queue:
                _, c = queue[0]
                if char_nums[c] > 0:
                    queue.popleft()
                    char_nums[c] -= 1
                else:
                    break

        def contains_all():
            """
            判断是否包含了 t 中的所有字符。第一次满足之后，后面肯定持续满足。
            """
            return all(v >= 0 for v in char_nums.values())

        ca = False
        ans = ""
        for i, c in enumerate(s):
            if c in char_nums:
                char_nums[c] = char_nums.get(c, 0) + 1
                queue.append((i, c))
                try_clean_queue()
            if ca or (ca := contains_all()):
                if not ans or i - queue[0][0] < len(ans):
                    ans = s[queue[0][0] : i + 1]
        return ans


import unittest


class TestSolution(unittest.TestCase):
    def test_minWindow(self):
        solution = Solution()
        self.assertEqual(solution.minWindow("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(solution.minWindow("A", "AA"), "")


if __name__ == "__main__":
    unittest.main()
