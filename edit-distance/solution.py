# -*- coding: utf-8 -*-

'''
https://leetcode-cn.com/problems/edit-distance/

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

1. Insert a character
2. Delete a character
3. Replace a character

Example 1:

    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation:
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')

Example 2:

    Input: word1 = "intention", word2 = "execution"
    Output: 5
    Explanation:
    intention -> inention (remove 't')
    inention -> enention (replace 'i' with 'e')
    enention -> exention (replace 'n' with 'x')
    exention -> exection (replace 'n' with 'c')
    exection -> execution (insert 'u')
'''


class Solution:
    def cache(func):
        cache = {}

        def inner(*args, **kargs):
            key = tuple(args[1:])
            if key in cache:
                return cache[key]

            r = func(*args, **kargs)
            cache[key] = r
            return r

        return inner

    @cache
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)

        if word1[-1] == word2[-1]:
            return min(
                self.minDistance(word1[:-1], word2[:-1]),
                self.minDistance(word1[:-1], word2[:-1])+1,
                self.minDistance(word1[:-1], word2)+1
            )

        return min(
            self.minDistance(word1, word2[:-1])+1,
            self.minDistance(word1[:-1], word2[:-1])+1,
            self.minDistance(word1[:-1], word2)+1
        )

        return r


def main():
    s = Solution()
    d = s.minDistance('horse', 'ros')
    assert d == 3

    d = s.minDistance('intention', 'execution')
    assert d == 5


if __name__ == '__main__':
    main()
