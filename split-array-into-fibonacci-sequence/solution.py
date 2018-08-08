# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/split-array-into-fibonacci-sequence/description/

Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]
Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]
Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.
Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
Note:

1 <= S.length <= 200
S contains only digits.
"""


class Solution(object):
    def hasLast2Nums(self, S, sumValue):
        """
        rtype: length, numA, numB
        >>> s = Solution()
        >>> s.hasLast2Nums("112358", 13)
        (2, 5, 8)
        >>> s.hasLast2Nums("112358", 18)
        (0, None, None)
        """
        for i in range(1, len(S)):
            x = int(S[-i:])
            if x > sumValue:
                break
            y = sumValue - x
            yStr = str(y)
            if S[:-i].endswith(yStr):
                return i+len(yStr), y, x
        return 0, None, None

    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        for i in range(1, 1+(len(S)+1)/2):
            last_num = int(S[-i:])
            if last_num >= 2147483648:
                return []
            rst = [last_num]
            # print last_num
            l, x, y = self.hasLast2Nums(S[:-i], last_num)
            # print l, x, y
            if l > 0:
                rst.insert(0, y)
                rst.insert(0, x)
                length = i+l
                while True:
                    if length == len(S):
                        return rst
                    d, dStr = y-x, str(y-x)
                    if not S[:-length].endswith(dStr):
                        break
                    length += len(dStr)
                    x, y = d, x
                    rst.insert(0, x)
        return []


def main():
    s = Solution()
    print s.splitIntoFibonacci("123456579")
    print s.splitIntoFibonacci("11235813")
    print s.splitIntoFibonacci("1101111")
    print s.splitIntoFibonacci("112358130")
    print s.splitIntoFibonacci("0123")
    print s.splitIntoFibonacci("011235")
    print s.splitIntoFibonacci("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511")


if __name__ == '__main__':
    main()
