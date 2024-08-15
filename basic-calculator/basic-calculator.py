#!/usr/bin/env python3

"""
https://leetcode.cn/problems/basic-calculator/
"""


class Solution:
    def read(self, s: str):
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            if not s[i].isdigit():
                return s[i], s[i + 1 :]
            j = i
            while i < len(s) and s[i].isdigit():
                i += 1
            return int(s[j:i]), s[i:]
        return None, s[i:]

    def simple_calculate(self, st: list) -> int:
        """
        only + and -
        """
        # print(st)
        s = 0
        while st:
            i = st.pop()
            if st:
                o = st.pop()
            else:
                o = "+"
            if o == "+":
                s += i
            elif o == "-":
                s -= i
        return s

    def calculate(self, s: str) -> int:
        st = []
        while s:
            o, s = self.read(s)
            # print(o, s, st)
            if o is None:
                break
            if o == "(":
                st.append(o)
            elif o == ")":
                simple_st = []
                while st[-1] != "(":
                    simple_st.insert(0, st.pop())
                st.pop()
                st.append(self.simple_calculate(simple_st))
            elif isinstance(o, str) and o in "+-*/":
                st.append(o)
            elif isinstance(o, int):
                if st and st[-1] == "*":
                    st.pop()
                    st.append(st.pop() * o)
                elif st and st[-1] == "/":
                    st.pop()
                    st.append(st.pop() / o)
                else:
                    st.append(o)
        return self.simple_calculate(st)


import unittest


class TestSolution(unittest.TestCase):
    def test_read(self):
        solution = Solution()
        self.assertEqual(solution.read("1 + 1"), (1, " + 1"))
        self.assertEqual(solution.read(" + 1"), ("+", " 1"))
        self.assertEqual(solution.read(" 1"), (1, ""))
        self.assertEqual(solution.read(" "), (None, ""))
        self.assertEqual(solution.read(""), (None, ""))

    def test_simple_calculate(self):
        solution = Solution()
        self.assertEqual(solution.simple_calculate([1, "+", 11, "-", 3]), 9)
        self.assertEqual(solution.simple_calculate(["-", 10, "+", 10]), 0)
        self.assertEqual(solution.simple_calculate([10, "+", 10]), 20)

    def test_calculate(self):
        solution = Solution()
        self.assertEqual(solution.calculate("(1+(4+5*2)-3)+(6+8)"), 26)
        self.assertEqual(solution.calculate("(1+(4+5+2)-3)+(6+8)"), 23)
        self.assertEqual(solution.calculate("1 + 1"), 2)
        self.assertEqual(solution.calculate(" 2-1 + 2 "), 3)


if __name__ == "__main__":
    unittest.main()
