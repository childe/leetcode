#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/open-the-lock/description/

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:
Input: deadends = ["0000"], target = "8888"
Output: -1
Note:
The length of deadends will be in the range [1, 500].
target will not be in the list deadends.
Every string in deadends and the string target will be a string of 4 digits from the 10,000 possibilities '0000' to '9999'.
'''


class Solution(object):
    def nextNodes(self, node, deadends):
        """
        :type node: str
        :type deadends: List[str]
        :rtype: [str]

        >>> s = Solution()
        >>> sorted(list(s.nextNodes('0000', ['0001', '0090'])))
        ['0009', '0010', '0100', '0900', '1000', '9000']
        """
        rst = set()
        for i, c in enumerate(node):
            n = int(c)
            up = (n+1) % 10
            up = node[:i]+str(up)+node[i+1:]
            down = (n-1) % 10
            down = node[:i]+str(down)+node[i+1:]

            if up not in deadends:
                rst.add(up)
            if down not in deadends:
                rst.add(down)

        return rst

    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        >>> s = Solution()
        >>> s.openLock(["0201","0101","0102","1212","2002"], target = "0202")
        6
        >>> s.openLock(deadends = ["8888"], target = "0009")
        1
        >>> s.openLock(deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888")
        -1
        >>> s.openLock(deadends = ["0000"], target = "8888")
        -1
        """

        if '0000' in deadends:
            return -1

        if '0000' == target:
            return 0

        # init
        nodes = [('0000', 0)]
        visited = set(deadends)

        # bfs
        idx = 0
        while idx < len(nodes):
            node, steps = nodes[idx]
            idx += 1
            if node == target:
                return steps
            if node in visited:
                continue
            visited.add(node)
            for node in self.nextNodes(node, visited):
                nodes.append( (node, steps+1))
        return -1


if __name__ == '__main__':
    s = Solution()
    import time
    print time.time()
    print s.openLock(["0201", "0101", "0102", "1212", "2002"], target="0202")
    print s.openLock(deadends=["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], target="8888")
    print time.time()
