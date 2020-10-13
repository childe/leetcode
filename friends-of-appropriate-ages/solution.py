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

"""


class Solution(object):
    def ifFriendRequest(self, a, b):
        # if b > a:
        # return False
        if b <= 0.5 * a + 7:
            return False
        return True

    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        if len(ages) < 2:
            return 0

        ageCount = {}
        for a in ages:
            ageCount.setdefault(a, 0)
            ageCount[a] += 1

        uages = list(ageCount.keys())
        uages.sort()
        uages.reverse()
        # print("!", uages)

        cache = set()
        for i, a in enumerate(uages):
            for b in uages[i:]:
                if self.ifFriendRequest(a, b):
                    cache.add((a, b))
        # print(cache)

        rst = 0
        for a, b in cache:
            if a == b:
                c = ageCount[a]
                rst += (c - 1) * c
            else:
                rst += ageCount[a] * ageCount[b]

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

    for l in open("./input").readlines():
        ans = s.numFriendRequests([int(e) for e in l.strip().split(",")])
        print(ans)


if __name__ == "__main__":
    main()
