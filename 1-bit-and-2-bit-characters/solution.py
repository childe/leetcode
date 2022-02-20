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
        s = [len(bits) - 2]
        while s:
            i = s.pop()
            if i == -1:
                return True

            if bits[i] == 0:
                s.append(i - 1)
                if i >= 1 and bits[i - 1] == 1:
                    s.append(i - 2)
            else:
                if i >= 1 and bits[i - 1] == 1:
                    s.append(i - 2)
        return False
