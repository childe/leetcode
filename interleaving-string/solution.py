# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/interleaving-string/

给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出: true
示例 2:

输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/interleaving-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        return self.isInterleaveR(s1, s2, s3)

    def isInterleaveR(self, s1, s2, s3):
        if s2 == "":
            return s1 == s3
        if s1 == "":
            return s2 == s3

        if s1[0] == s3[0]:
            if s2[0] != s3[0]:
                return self.isInterleaveR(s1[1:], s2, s3[1:])
            return self.isInterleaveR(s1[1:], s2, s3[1:]) or self.isInterleaveR(
                s1, s2[1:], s3[1:]
            )
        if s2[0] == s3[0]:
            return self.isInterleaveR(s1, s2[1:], s3[1:])
        return False


def main():
    """docstring for main"""
    s = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    ans = s.isInterleave(s1, s2, s3)
    assert ans is True

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    ans = s.isInterleave(s1, s2, s3)
    assert ans is False


if __name__ == "__main__":
    main()
