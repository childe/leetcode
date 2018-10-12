# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/possible-bipartition/description/

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group.

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.



Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false


Note:

1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
"""


class Solution(object):
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        graph = [None] * (1+N)
        for i in range(1, 1+N):
            graph[i] = [0] * (1+N)

        for x, y in dislikes:
            graph[x][y] = graph[y][x] = 1

        not_visited = set(range(1, 1+N))

        while not_visited:
            groupA, groupB, visited = set(), set(), set()
            groupA.add(not_visited.pop())

            while groupA.difference(visited) or groupB.difference(visited):
                for n in groupA.difference(visited):
                    visited.add(n)
                    for i in range(1, N+1):
                        if graph[n][i]:
                            if i in groupA:
                                return False
                            groupB.add(i)

                for n in groupB.difference(visited):
                    visited.add(n)
                    for i in range(1, N+1):
                        if graph[n][i]:
                            if i in groupB:
                                return False
                            groupA.add(i)
            not_visited.difference_update(visited)

        return True


if __name__ == '__main__':
    s = Solution()
    print s.possibleBipartition(N=4, dislikes=[[1, 2]]) is True
    print s.possibleBipartition(N=4, dislikes=[[1, 2], [1, 3], [2, 4]]) is True
    print s.possibleBipartition(N=3, dislikes=[[1, 2], [1, 3], [2, 3]]) is False
    print s.possibleBipartition(N=5, dislikes=[[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]) is False
    print s.possibleBipartition(N=5, dislikes=[[1, 2], [3, 4], [4, 5], [3, 5]]) is False

    for i, line in enumerate(open('input.txt').readlines()):
        if line.strip().startswith('#'):
            continue
        if i % 3 == 0:
            result = 'TRUE'.startswith(line.strip().upper())
        elif i % 3 == 1:
            N = int(line.strip())
        else:
            dislikes = eval(line.strip())
            print s.possibleBipartition(N, dislikes) is result
