#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/maximum-number-of-weeks-for-which-you-can-work/

1953. Maximum Number of Weeks for Which You Can Work
There are n projects numbered from 0 to n - 1. You are given an integer array milestones where each milestones[i] denotes the number of milestones the ith project has.

You can work on the projects following these two rules:

Every week, you will finish exactly one milestone of one project. You must work every week.
You cannot work on two milestones from the same project for two consecutive weeks.
Once all the milestones of all the projects are finished, or if the only milestones that you can work on will cause you to violate the above rules, you will stop working. Note that you may not be able to finish every project's milestones due to these constraints.

Return the maximum number of weeks you would be able to work on the projects without violating the rules mentioned above.

 

Example 1:

Input: milestones = [1,2,3]
Output: 6
Explanation: One possible scenario is:
- During the 1st week, you will work on a milestone of project 0.
- During the 2nd week, you will work on a milestone of project 2.
- During the 3rd week, you will work on a milestone of project 1.
- During the 4th week, you will work on a milestone of project 2.
- During the 5th week, you will work on a milestone of project 1.
- During the 6th week, you will work on a milestone of project 2.
The total number of weeks is 6.

Example 2:

Input: milestones = [5,2,1]
Output: 7
Explanation: One possible scenario is:
- During the 1st week, you will work on a milestone of project 0.
- During the 2nd week, you will work on a milestone of project 1.
- During the 3rd week, you will work on a milestone of project 0.
- During the 4th week, you will work on a milestone of project 1.
- During the 5th week, you will work on a milestone of project 0.
- During the 6th week, you will work on a milestone of project 2.
- During the 7th week, you will work on a milestone of project 0.
The total number of weeks is 7.
Note that you cannot work on the last milestone of project 0 on 8th week because it would violate the rules.
Thus, one milestone in project 0 will remain unfinished.
 

Constraints:

n == milestones.length
1 <= n <= 10^5
1 <= milestones[i] <= 10^9
"""


class Solution:
    def numberOfWeeks(self, milestones: list[int]) -> int:
        """
        >>> s = Solution()
        >>> s.numberOfWeeks([1,10,7,1,7,2,10,10,355359359])
        97
        >>> s.numberOfWeeks([1])
        1
        >>> s.numberOfWeeks([1,2,3])
        6
        >>> s.numberOfWeeks([5,2,1])
        7
        >>> s.numberOfWeeks([5,5,5])
        15
        """
        total = sum(milestones)
        milestones.sort()

        milestones = [e for e in milestones if e > 0]
        if len(milestones) == 1:
            return 1

        while len(milestones) > 1:
            # print(milestones)
            haveRemoved = 0
            for i, n in enumerate(milestones):
                # print(i, n, haveRemoved)
                if i == 0:
                    milestones[i] = 0
                    haveRemoved = n
                    continue
                if (n - haveRemoved) < milestones[i - 1]:
                    milestones[i] = milestones[i - 1]
                    haveRemoved += n - milestones[i - 1]
                else:
                    milestones[i] -= haveRemoved
                    haveRemoved += haveRemoved
            milestones = [e for e in milestones if e > 0]

        # print(milestones)
        if len(milestones) > 0:
            return total - sum(milestones) + 1
        else:
            return total - sum(milestones)
