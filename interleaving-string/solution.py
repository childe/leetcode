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

        visited = set((0, 0, 0))
        bfs_stack = [(0, 0, 0)]
        while bfs_stack:
            print(len(bfs_stack))
            i, j, k = bfs_stack.pop()
            if i == len(s1):
                if s2[j:] == s3[k:]:
                    return True
            elif s1[i] == s3[k]:
                n = (i + 1, j, k + 1)
                if n not in visited:
                    visited.add(n)
                    bfs_stack.insert(0, n)
            if j == len(s2):
                if s1[i:] == s3[k:]:
                    return True
            elif s2[j] == s3[k]:
                n = (i, j + 1, k + 1)
                if n not in visited:
                    visited.add(n)
                    bfs_stack.insert(0, n)

        return False


def create_s3():
    import random
    import string

    s1 = "".join([random.choice(string.ascii_lowercase) for i in range(20)])
    s2 = "".join([random.choice(string.ascii_lowercase) for i in range(20)])

    s3 = ""
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if random.random() < 0.5:
            s3 += s1[i]
            i += 1
        else:
            s3 += s2[j]
            j += 1

    s3 += s1[i:]
    s3 += s2[j:]
    return s1, s2, s3


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

    import random

    for i in range(100):
        s1, s2, s3 = create_s3()
        # print(s1, s2, s3)
        ans = s.isInterleave(s1, s2, s3)
        assert ans is True
        t = list(s3)
        random.shuffle(t)
        s3 = "".join(t)
        ans = s.isInterleave(s1, s2, s3)
        assert ans is False

    s1 = "a" * 20 + "b"
    s2 = "a" * 20 + "c"
    s3 = "a" * 40 + "bc"
    s3 = s3[: len(s1) + len(s2)]
    ans = s.isInterleave(s1, s2, s3)
    assert ans is True

    s1 = "a" * 20 + "b"
    s2 = "a" * 20 + "c"
    s3 = "a" * 40 + "xy"
    s3 = s3[: len(s1) + len(s2)]
    ans = s.isInterleave(s1, s2, s3)
    assert ans is False

if __name__ == "__main__":
    main()
