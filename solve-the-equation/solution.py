# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/solve-the-equation/

640. Solve the Equation

Solve a given equation and return the value of x in the form of string "x=#value".
The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"
"""


class Solution(object):
    def parse(self, e):
        # print(e)
        if not e:
            return 0, 0

        if e[-1] == "x":
            if e == "x":
                return 1, 0
            elif e == "-x":
                return -1, 0
            elif e == "+x":
                return 1, 0
            else:
                return int(e[:-1]), 0
        else:
            return 0, int(e)

    def parseHalf(self, exp):
        """
        解析=左边或者右边的
        return (coefficient,const)
        """
        coefficient, const = 0, 0
        e = ""
        for c in exp:
            if c == "+" or c == "-":
                if e != "":  # 最前面的符号
                    a, b = self.parse(e)
                    coefficient += a
                    const += b
                e = ""
            e += c

        a, b = self.parse(e)
        coefficient += a
        const += b

        return coefficient, const

    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left, right = equation.split("=")
        left_coefficient, left_const = self.parseHalf(left)
        # print(left_coefficient, left_const)
        right_coefficient, right_const = self.parseHalf(right)
        # print(right_coefficient, right_const)

        coefficient = left_coefficient - right_coefficient
        const = right_const - left_const
        if coefficient == 0:
            return "Infinite solutions" if const == 0 else "No solution"
        return "x={}".format(const // coefficient)


def main():
    s = Solution()

    ans = s.solveEquation("x+5-3+x=6+x-2")
    print(ans)
    assert ans == "x=2"

    ans = s.solveEquation("x=x")
    print(ans)
    assert ans == "Infinite solutions"

    ans = s.solveEquation("x=2x")
    print(ans)
    assert ans == "x=0"

    ans = s.solveEquation("2x+3x-6x=x+2")
    print(ans)
    assert ans == "x=-1"

    ans = s.solveEquation("x=x+2")
    print(ans)
    assert ans == "No Solution"


if __name__ == "__main__":
    main()
