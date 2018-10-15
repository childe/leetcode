# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/fruit-into-baskets/description/

In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.

Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2,
then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?



Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.


Note:

1 <= tree.length <= 40000
0 <= tree[i] < tree.length
"""


class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        last_pos = [None] * len(tree)
        last_pos[0] = 0
        for i in range(1, len(tree)):
            if tree[i] == tree[i-1]:
                last_pos[i] = last_pos[i-1]
            else:
                last_pos[i] = i

        buckets = [None] * len(tree)
        for i in range(len(tree)):
            buckets[i] = set()
        max_fruits = [0] * len(tree)
        buckets[0].add(tree[0])
        max_fruits[0] = 1

        for i in range(1, len(tree)):
            if tree[i] in buckets[i-1]:
                buckets[i] = buckets[i-1]
                max_fruits[i] = max_fruits[i-1]+1
            else:
                buckets[i] = set([tree[i-1], tree[i]])
                max_fruits[i] = i - last_pos[i-1] + 1

        return max(max_fruits)


if __name__ == '__main__':
    s = Solution()
    print s.totalFruit([1, 2, 1]) == 3
    print s.totalFruit([0, 1, 2, 2]) == 3
    print s.totalFruit([1, 2, 3, 2, 2]) == 4
    print s.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5
