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
        # st = {}
        # for c in t:
        # st[c] += st.get(c, 0) + 1
        char_nums = {}
        for c in t:
            char_nums[c] = char_nums.get(c, 0) - 1
        queue = deque()

        def try_clean_queue():
            while queue:
                _, c = queue[0]
                if char_nums[c] > 0:
                    queue.popleft()
                    char_nums[c] -= 1
                else:
                    break

        _contains_all = False

        def contains_all():
            nonlocal _contains_all
            if _contains_all:
                return True
            for v in char_nums.values():
                if v < 0:
                    return False
            _contains_all = True
            return True

        ans = ""
        for i, c in enumerate(s):
            if c in char_nums:
                char_nums[c] = char_nums.get(c, 0) + 1
                queue.append((i, c))
                try_clean_queue()
            if contains_all():
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
