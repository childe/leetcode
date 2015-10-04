#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a digit string, return all possible letter combinations
that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is
given below.


Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be
in any order you want.
"""
import unittest


class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        charmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"}

        if digits == "":
            return []
        strs = [charmap[d] for d in digits]
        #print strs

        rst = []

        #[0,0,0] means output the first char of each str
        char_indices = [0] * len(digits)

        overflow = False
        while not overflow:
            #print char_indices
            rst.append("".join([strs[idx][i]
                       for idx, i in enumerate(char_indices)]))

            # last char_index +=1
            cureent_str_idx = len(digits)-1
            char_indices[cureent_str_idx] += 1

            while(char_indices[cureent_str_idx] >= len(strs[cureent_str_idx])):
                if cureent_str_idx == 0:
                    overflow = True
                    break
                char_indices[cureent_str_idx] = 0
                cureent_str_idx -= 1
                char_indices[cureent_str_idx] += 1

        return rst


class TestSolution(unittest.TestCase):

    def test_letterCombinations(self):
        s = Solution()

        my_answer = s.letterCombinations("")
        answer = []
        self.assertEqual(my_answer, answer)

        my_answer = s.letterCombinations("9")
        answer = ["w", "x", "y", "z"]
        self.assertEqual(my_answer, answer)

        my_answer = s.letterCombinations("23")
        answer = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(my_answer, answer)

        charmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"}
        import random
        digits = ''.join([
            random.choice
            (['2', '3', '4', '5', '6', '7', '8', '9'])
            for i in range(random.randint(0, 10))])
        #print digits
        my_answer = s.letterCombinations(digits)
        #print my_answer

        l = 1
        for d in digits:
            l *= len(charmap[d])
        self.assertEqual(len(my_answer), l)

        for a in my_answer:
            for idx,c in enumerate(a):
                self.assertTrue(c in charmap[digits[idx]])


if __name__ == '__main__':
    unittest.main()
