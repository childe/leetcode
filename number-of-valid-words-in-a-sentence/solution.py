#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/number-of-valid-words-in-a-sentence/

A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only. Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.

A token is a valid word if all three of the following are true:

It only contains lowercase letters, hyphens, and/or punctuation (no digits).
There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters ("a-b" is valid, but "-ab" and "ab-" are not valid).
There is at most one punctuation mark. If present, it must be at the end of the token ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).
Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".

Given a string sentence, return the number of valid words in sentence.

 

Example 1:

Input: sentence = "cat and  dog"
Output: 3
Explanation: The valid words in the sentence are "cat", "and", and "dog".

Example 2:

Input: sentence = "!this  1-s b8d!"
Output: 0
Explanation: There are no valid words in the sentence.
"!this" is invalid because it starts with a punctuation mark.
"1-s" and "b8d" are invalid because they contain digits.

Example 3:

Input: sentence = "alice and  bob are playing stone-game10"
Output: 5
Explanation: The valid words in the sentence are "alice", "and", "bob", "are", and "playing".
"stone-game10" is invalid because it contains digits.
 

Constraints:

1 <= sentence.length <= 1000
sentence only contains lowercase English letters, digits, ' ', '-', '!', '.', and ','.
There will be at least 1 token.
"""


class Solution:
    def if_valid_word(self, word: str) -> bool:
        """
        >>> s = Solution()
        >>> s.if_valid_word('!this')
        False
        >>> s.if_valid_word('1-s!')
        False
        >>> s.if_valid_word('b8d!')
        False
        >>> s.if_valid_word('stone-game10')
        False
        >>> s.if_valid_word('dog')
        True
        """
        l = len(word)
        hyphen_count = 0
        for i, c in enumerate(word):
            if "0" <= c <= "9":
                return False
            if c in (".", ",", "!"):
                if i == l - 1:
                    return True
                return False
            if c == "-":
                if hyphen_count == 1:
                    return False
                if i == 0 or i == l - 1:
                    return False
                if word[i - 1] < "a" or word[i - 1] > "z":
                    return False
                if word[i + 1] < "a" or word[i + 1] > "z":
                    return False
                hyphen_count += 1

        return True

    def countValidWords(self, sentence: str) -> int:
        """
        >>> s = Solution()
        >>> s.countValidWords(sentence = "cat and  dog")
        3
        >>> s.countValidWords(sentence = "!this  1-s b8d!")
        0
        >>> s.countValidWords(sentence = "alice and  bob are playing stone-game10")
        5
        """
        return len([w for w in sentence.split() if self.if_valid_word(w)])
