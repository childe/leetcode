#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/regular-expression-matching/

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""
import unittest


class Solution:

    def _preprocess(self, p):
        """
        :type p: str
        :rtype: str
        """
        r = ""
        successive_char = ""
        successive=0
        has_star = False
        for idx,e in enumerate(p):
            if e=="*":
                if idx==0 or p[idx-1]=="*":
                    return False
                has_star = True
                successive-=1
            elif successive_char=="" or e == successive_char:
                successive_char=e
                successive+=1
            else:
                r+=successive_char*successive
                if has_star:
                    r+=successive_char+"*"
                successive_char = e
                successive=1
                has_star=False

        r+=successive_char*successive
        if has_star:
            r+=successive_char+"*"

        return r



    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p = self._preprocess(p)
        if p is False:
            return False

        if s == "" :
            if len(p)%2==0 and p[1::2].count("*") == len(p)/2:
                return True
            return False

        if p=="" or p[0]=="*":
            return False

        l = []  # s_unit, p_unit, rest_s, rest_p
        if p[1:] and p[1] == "*":
            l.append(("", p[:2], s, p[2:]))
            for idx, e in enumerate(s):
                if p[0] == "." or p[0] == e:
                    l.append((s[:idx+1], p[:2], s[idx+1:], p[2:]))
                else:
                    break
        else:
            if p[0] == "." or p[0] == s[0]:
                l.append((s[0], p[0], s[1:], p[1:]))

        #i = 0
        while l:
            #print i,
            #i+=1
            #print l
            s_unit, p_unit, s, p = l.pop()

            if s == "" :
                if len(p)%2==0 and p[1::2].count("*") == len(p)/2:
                    return True
                continue

            if p=="" or p[0]=="*":
                continue


            if p[1:] and p[1] == "*":
                l.append(("", p[:2], s, p[2:]))
                for idx, e in enumerate(s):
                    if p[0] == "." or p[0] == e:
                        l.append((s[:idx+1], p[:2], s[idx+1:], p[2:]))
                    else:
                        break
            else:
                if p[0] == "." or p[0] == s[0]:
                    l.append((s[0], p[0], s[1:], p[1:]))

        return False


class TestSolution(unittest.TestCase):

    def no_test_preprocess(self):
        s = Solution()

        self.assertEqual("...*c*", s._preprocess(".*..c*"))
        self.assertEqual(False, s._preprocess("*"))
        self.assertEqual(False, s._preprocess("**"))
        self.assertEqual(False, s._preprocess("**a*"))
        self.assertEqual(False, s._preprocess("a**a*"))
        self.assertEqual("a*", s._preprocess("a*a*"))
        self.assertEqual("a*", s._preprocess("a*a*a*"))
        self.assertEqual("aaaaa*", s._preprocess("a*aaa*aaa*"))
        self.assertEqual("a*", s._preprocess("a*a*a*a*"))
        self.assertEqual("aaaa*", s._preprocess("aaaa*"))
        self.assertEqual("aaa*", s._preprocess("a*aaa*"))
        self.assertEqual(".*", s._preprocess(".*.*"))
        self.assertEqual(".*", s._preprocess(".*.*.*"))
        self.assertEqual("a.*", s._preprocess("a.*.*.*"))
        self.assertEqual("a.*a", s._preprocess("a.*.*.*a"))
        self.assertEqual("a.*b", s._preprocess("a.*.*.*b"))

    def test_isMatch(self):
        s = Solution()

        self.assertTrue(s.isMatch("", "a*c*"))
        self.assertTrue(s.isMatch("ab", "...*c*"))
        self.assertTrue(s.isMatch("ab", ".*..c*"))
        self.assertTrue(s.isMatch("", ""))
        self.assertFalse(s.isMatch("aa", ""))
        self.assertFalse(s.isMatch("", "aa"))
        self.assertFalse(s.isMatch("a", "ab*a"))
        self.assertTrue(s.isMatch("aa", "aa"))
        self.assertTrue(s.isMatch("aa", "a*"))
        self.assertTrue(s.isMatch("aa", ".a"))
        self.assertFalse(s.isMatch("ab", ".a"))
        self.assertTrue(s.isMatch("aab", "c*a*b"))
        self.assertFalse(s.isMatch("aaa", "aa"))
        self.assertTrue(s.isMatch("fasjdiuroutrejaab", ".*"))
        self.assertTrue(s.isMatch("bbbba", ".*a*a"))
        self.assertFalse(s.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"))

        import random
        import re
        candidates = ("a","b",)

        for n in range(100):
            string = ""
            for i in range(30):
                string += random.choice(candidates)
            p=""
            for j in range(30):
                p += random.choice(candidates+(".","*"))
            p = p.replace("**","").strip("*")
            #print string,p
            rst = re.match("^"+p+"$",string) is not None
            self.assertEqual(rst, s.isMatch(string, p))



if __name__ == '__main__':
    unittest.main()
