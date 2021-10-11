# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/nearest-exit-from-entrance-in-maze/

You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.


Example 1:
Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.


Example 2:
Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.

Example 3:
Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.

Constraints:

maze.length == m
maze[i].length == n
1 <= m, n <= 100
maze[i][j] is either '.' or '+'.
entrance.length == 2
0 <= entrancerow < m
0 <= entrancecol < n
entrance will always be an empty cell.
"""


class Solution:
    def isBordor(self, position, m, n):
        x, y = position
        if x == 0 or y == 0:
            return True
        if x == m - 1 or y == n - 1:
            return True
        return False

    def isEmptyCell(self, position, maze):
        m, n = len(maze), len(maze[0])
        x, y = position
        if x < 0 or x >= m:
            return False
        if y < 0 or y >= n:
            return False

        return maze[x][y] == "."

    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        m, n = len(maze), len(maze[0])
        visited = set()
        visited.add(tuple(entrance))
        s = [(tuple(entrance), int(0))]
        while s:
            # print(s)
            position, steps = s.pop()
            x, y = position
            # print(x, y)
            if steps > 0 and self.isBordor(position, m, n):
                # print(x, y, steps)
                return steps

            for new_position in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if self.isEmptyCell(new_position, maze):
                    if new_position not in visited:
                        visited.add(new_position)
                        s.insert(0, (new_position, steps + 1))

        return -1


def main():
    s = Solution()

    maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
    entrance = [1, 2]
    ans = s.nearestExit(maze, entrance)
    print(ans)
    assert ans == 1

    maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
    entrance = [1, 0]
    ans = s.nearestExit(maze, entrance)
    print(ans)
    assert ans == 2

    maze = [[".", "+"]]
    entrance = [0, 0]
    ans = s.nearestExit(maze, entrance)
    print(ans)
    assert ans == -1

    maze = [
        ["+", ".", "+", "+", "+", "+", "+"],
        ["+", ".", "+", ".", ".", ".", "+"],
        ["+", ".", "+", ".", "+", ".", "+"],
        ["+", ".", ".", ".", "+", ".", "+"],
        ["+", "+", "+", "+", "+", ".", "+"],
    ]
    entrance = [0, 1]
    ans = s.nearestExit(maze, entrance)
    print(ans)
    assert ans == 12


if __name__ == "__main__":
    main()
