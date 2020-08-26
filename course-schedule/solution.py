# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/course-schedule/

207. Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is
expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a
graph is represented.

You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        could_not = set(p[0] for p in prerequisites)
        could = set(range(0, numCourses)).difference(could_not)

        prerequisites_dict = {}
        reverse_prerequisites_dict = {}
        for c1, c2 in prerequisites:
            prerequisites_dict.setdefault(c1, set())
            reverse_prerequisites_dict.setdefault(c2, set())
            prerequisites_dict[c1].add(c2)
            reverse_prerequisites_dict[c2].add(c1)

        while could:
            c = could.pop()
            for cc in reverse_prerequisites_dict.get(c, set()):
                prerequisites_dict[cc].remove(c)
                if not prerequisites_dict[cc]:
                    could.add(cc)
                    could_not.remove(cc)

        return len(could_not) == 0
