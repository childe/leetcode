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
    def printdp(self, dp):
        for row in dp:
            print(row)
        print()

    def minDistance(self, word1: str, word2: str) -> int:
        dp = [None] * (1+len(word1))
        for i in range(1+len(word1)):
            dp[i] = [None] * (1+len(word2))
            dp[i][0] = i
        for j in range(1+len(word2)):
            dp[0][j] = j

        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = min(
                        dp[i][j],
                        dp[i][j+1]+1,
                        dp[i+1][j]+1
                    )
                else:
                    dp[i+1][j+1] = min(
                        dp[i][j]+1,
                        dp[i][j+1]+1,
                        dp[i+1][j]+1
                    )

        return dp[len(word1)][len(word2)]


def main():
    s = Solution()
    d = s.minDistance('horse', 'ros')
    print(d)
    assert d == 3

    d = s.minDistance('intention', 'execution')
    print(d)
    assert d == 5


if __name__ == '__main__':
    main()
