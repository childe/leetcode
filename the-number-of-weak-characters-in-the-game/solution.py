#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/the-number-of-weak-characters-in-the-game/

You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

Return the number of weak characters.

 

Example 1:

Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.

Example 2:

Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.

Example 3:

Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.
 

Constraints:

2 <= properties.length <= 10^5
properties[i].length == 2
1 <= attacki, defensei <= 10^5
"""


class Solution:
    def numberOfWeakCharacters(self, properties: list[list[int]]) -> int:
        """
        >>> s = Solution()
        >>> s.numberOfWeakCharacters(properties = [[5,5],[6,3],[3,6]])
        0
        >>> s.numberOfWeakCharacters(properties = [[2,2],[3,3]])
        1
        >>> s.numberOfWeakCharacters(properties = [[1,5],[10,4],[4,3]])
        1
        >>> s.numberOfWeakCharacters([[1,1],[2,1],[2,2],[1,2]])
        1
        >>> s.numberOfWeakCharacters([[7,7],[1,2],[9,7],[7,3],[3,10],[9,8],[8,10],[4,3],[1,5],[1,5]])
        6
        """
        # init m
        m = {}
        for p in properties:
            m.setdefault(p[0], list())
            m[p[0]].append(p[1])

        for k, v in m.items():
            m[k] = sorted(v)

        attacks = sorted(m.keys())

        # init max_defence_map
        max_defence_value = 0
        max_defence_map = {}
        for i, attack in enumerate(attacks[::-1]):
            max_defence_value = max(max_defence_value, m[attack][-1])
            max_defence_map[attack] = max_defence_value

        count = 0
        for i, attack in enumerate(attacks[:-1]):
            next_attack = attacks[i + 1]
            max_defence_from_next_attack = max_defence_map[next_attack]
            defence_values = m[attack]
            for j, defence in enumerate(defence_values[::-1]):
                if defence < max_defence_from_next_attack:
                    break
            else:
                j = len(defence_values)

            count += len(defence_values) - j

        return count


def main():
    properties = eval(open("./input").read())
    print(len(properties))
    s = Solution()
    s.numberOfWeakCharacters(properties)


if __name__ == "__main__":
    main()
