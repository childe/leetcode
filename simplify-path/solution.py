# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/simplify-path/description/

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        >>> s = Solution()
        >>> s.simplifyPath("/home/")
        '/home'
        >>> s.simplifyPath("/a/./b/../../c/")
        '/c'
        >>> s.simplifyPath("/home//foo/")
        '/home/foo'
        >>> s.simplifyPath("/../")
        '/'
        """
        s = list()
        for p in path.split('/'):
            if p == '.' or p == '':
                continue
            elif p == '..':
                if s:
                    s.pop()
            else:
                s.append(p)

        return '/' + '/'.join(s)
