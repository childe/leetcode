# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/friends-of-appropriate-ages/

825. Friends Of Appropriate Ages
Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person.

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.

Example 2:

Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.
Example 3:

Input: [20,30,100,110,120]
Output: 3
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.

Notes:

1 <= ages.length <= 20000.
1 <= ages[i] <= 120.

随手写了几个, 都超时了. 试一下双指针吧, 应该是最快的算法了.
"""


class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        if len(ages) < 2:
            return 0

        ages.sort()
        rst = 0
        i, j, l = 0, 1, len(ages)

        while j < l:
            a = ages[i]
            b = ages[j]
            print(a, b, rst)
            if a <= 0.5 * b + 7:
                i += 1
                if i == j:
                    j += 1
            elif b == a:
                while j < l and a == ages[j]:
                    j += 1
                rst += (j - i) * (j - i - 1)
            else:
                rst += 1
                j += 1

        rst += (j - i - 2) * (j - i - 1) // 2
        return rst


def main():
    s = Solution()
    ans = s.numFriendRequests(
        [73, 106, 39, 6, 26, 15, 30, 100, 71, 35, 46, 112, 6, 60, 110]
    )
    print(ans)
    assert ans == 29

    ans = s.numFriendRequests([16, 16])
    print(ans)
    assert ans == 2

    ans = s.numFriendRequests([16, 17, 18])
    print(ans)
    assert ans == 2

    ans = s.numFriendRequests([20, 30, 100, 110, 120])
    print(ans)
    assert ans == 3


if __name__ == "__main__":
    main()
