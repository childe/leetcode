#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        >>> s = Solution()
        >>> s.compareVersion(version1 = "0.1", version2 = "1.1")
        -1
        >>> s.compareVersion(version1 = "1.0.1", version2 = "1")
        1
        >>> s.compareVersion(version1 = "7.5.2.4", version2 = "7.5.3")
        -1
        >>> s.compareVersion(version1 = "1", version2 = "0")
        1
        >>> s.compareVersion(version1 = "1", version2 = "1.1")
        -1
        >>> s.compareVersion(version1 = "01", version2 = "1")
        0
        >>> s.compareVersion(version1 = "1.0", version2 = "1")
        0
        >>> s.compareVersion(version1 = "1.0.0", version2 = "1")
        0
        >>> s.compareVersion(version1 = "1.0.0", version2 = "1.0")
        0
        >>> s.compareVersion(version1 = "1", version2 = "1.0")
        0
        """

        splited1 = version1.split('.')
        splited2 = version2.split('.')
        flag = 1
        if len(splited1) < len(splited2):
            splited1, splited2 = splited2, splited1
            flag = -1

        for i, e in enumerate(splited1):
            if not splited2[i:]:
                if int(e) > 0:
                    return 1 * flag
                continue
            if int(e) > int(splited2[i]):
                return 1 * flag
            if int(e) < int(splited2[i]):
                return -1 * flag

        return 0
