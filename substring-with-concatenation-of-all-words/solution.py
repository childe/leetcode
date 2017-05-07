#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
https://leetcode.com/problems/substring-with-concatenation-of-all-words

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
'''


from functools import reduce


class Solution(object):

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        >>> s = Solution()

        >>> s.findSubstring("barfoothefoobarman", ["foo", "bar"])
        [0, 9]

        >>> s.findSubstring("aaa", ["aa", "aa"])
        []

        >>> s.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"])
        [8]

        >>> s.findSubstring("a", ["a"])
        [0]

        >>> s.findSubstring("abababab", ["ab","ab","ab"])
        [0, 2]

        >>> s.findSubstring("ab"*5000, ["ab","ba"]*100)
        []
        """
        def judge(s):
            # print s,words
            return sorted(words) == sorted(
                [s[i * len(words[0]): (1 + i) * len(words[0])]
                 for i in range(len(words))])

        def exactly(s1, s2, length):
            return sorted([s1[i * length: (1 + i) * length] for i in range(len(s1)/length)]
                          ) == sorted([s2[i * length: (2 + i) * length] for i in range(len(s2)/length)])

        if words == []:
            return []
        if len(s) < len(words) * len(words[0]):
            return []

        pl = lambda l: reduce(lambda x, y: x*y, l)
        total_letter_length = len(words) * len(words[0])

        words = [map(lambda x:ord(x), word) for word in words]
        right_product = pl([pl(word) for word in words])
        # print right_product

        s = [ord(w) for w in s]
        product = pl(s[:total_letter_length])
        # print product

        rst = []
        for i, e in enumerate(s[:len(s)+1-total_letter_length]):
            if i > 0:
                product = product * s[i+total_letter_length-1] / s[i-1]
            # print i, product
            if product != right_product:
                continue
            for j in range(1, len(words)):
                if exactly( s [i + total_letter_length - j * len(words[0]): i + total_letter_length], s[i - j * len(words[0]): i], len(words[0])):
                    if (i - j * len(words[0])) in rst:
                        rst.append(i)
                    break
            else:
                if (rst == [] or rst[-1] != i) and judge(s[i: i+total_letter_length]):
                    rst.append(i)

        return rst
