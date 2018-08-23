# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/walking-robot-simulation/description/

A robot on an infinite grid starts at point (0, 0) and faces north.  The robot can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles.

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them, the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.



Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)


Note:

0 <= commands.length <= 10000
0 <= obstacles.length <= 10000
-30000 <= obstacle[i][0] <= 30000
-30000 <= obstacle[i][1] <= 30000
The answer is guaranteed to be less than 2 ^ 31.
"""


class Solution(object):
    def init_obstacles(self, obstacles):
        x, y = {}, {}
        for o in obstacles:
            x.setdefault(o[0], [])
            x[o[0]].append(o[1])

            y.setdefault(o[1], [])
            y[o[1]].append(o[0])

        for xi in x:
            x[xi].sort()
        for yi in y:
            y[yi].sort()

        self.obstacles = [x, y]  # obstacles[0] is [x1:[y1,y2...], x2:[y1,y2...]...]

    def find_stop(self, start, end, obstacles):
        """
        rtype: first obstacle
        >>> s = Solution()
        >>> s.find_stop(1, 10, [5])
        4
        >>> s.find_stop(1, 2, [1,2])
        1
        >>> s.find_stop(1, 10, [1,5,7,10])
        4
        >>> s.find_stop(1, 4, [0,5,7,10])
        4
        >>> s.find_stop(10, 1, [5])
        6
        >>> s.find_stop(2, 1, [1,2])
        2
        >>> s.find_stop(10, 1, [1,5,7,11])
        8
        >>> s.find_stop(4, 1, [1,5,7,10])
        2
        """
        if not obstacles:
            return end
        small, big = min(start, end), max(start, end)
        if small > obstacles[-1] or big < obstacles[0]:
            return end

        low, high = 0, len(obstacles)-1
        r = end
        if start < end:
            while low < high:
                mid = (low+high)/2
                if obstacles[mid] <= start:
                    low = mid+1
                elif obstacles[mid] > end:
                    high = mid-1
                else:
                    r = obstacles[mid]-1
                    high = mid-1
            if start < obstacles[high] <= end:
                return obstacles[high] - 1
        else:
            while low < high:
                mid = (low+high)/2
                if obstacles[mid] >= start:
                    high = mid-1
                elif obstacles[mid] < end:
                    low = mid+1
                else:
                    r = obstacles[mid]+1
                    low = mid+1
            if start > obstacles[high] >= end:
                return obstacles[high] + 1
        return r

    def move(self, distance):
        if distance == 0:
            return

        dx, dy = self.four_d[self.d][0], self.four_d[self.d][1]
        if dx == 0:
            end = self.y+dy*distance
            self.y = self.find_stop(self.y, end, self.obstacles[0].get(self.x, []))
        else:
            end = self.x+dx*distance
            self.x = self.find_stop(self.x, end, self.obstacles[1].get(self.y, []))

    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        self.four_d = ((0, 1), (1, 0), (0, -1), (-1, 0))
        self.x = 0
        self.y = 0
        self.d = 0
        self.init_obstacles(obstacles)

        maximum_distance = 0
        for comm in commands:
            if comm == -1:
                self.d = (self.d+1) % 4
            elif comm == -2:
                self.d = (self.d+3) % 4
            else:
                self.move(distance=comm)
                maximum_distance = max(maximum_distance, self.x**2 + self.y**2)

        return maximum_distance


def main():
    s = Solution()
    print s.robotSim([4, -1, 3], [])
    print s.robotSim(commands=[4, -1, 4, -2, 4], obstacles=[[2, 4]])


if __name__ == '__main__':
    main()
