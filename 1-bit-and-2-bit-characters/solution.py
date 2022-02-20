#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/

717. 1-bit and 2-bit Characters
We have two special characters:

The first character can be represented by one bit 0.
The second character can be represented by two bits (10 or 11).
Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

 

Example 1:

Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.
Example 2:

Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.
 

Constraints:

1 <= bits.length <= 1000
bits[i] is either 0 or 1.
"""


class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        """
        >>> s = Solution()
        >>> s.isOneBitCharacter([1,0,0])
        True
        >>> s.isOneBitCharacter([1,1,1,0])
        False
        """

        def recursion(i: int) -> bool:
            if i == -1:
                return True

            if i == 0:
                if bits[i] == 0:
                    return True
                else:
                    return False

            r = []
            if bits[i] == 0:
                r.append(recursion(i - 1))
                if bits[i - 1] == 1:
                    r.append(recursion(i - 2))
            else:
                if bits[i - 1] == 1:
                    r.append(recursion(i - 2))
            return any(r)

        return recursion(len(bits) - 2)
