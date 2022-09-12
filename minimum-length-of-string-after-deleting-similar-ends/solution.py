#!/usr/bin/env python3

"""
https://leetcode.cn/problems/minimum-length-of-string-after-deleting-similar-ends/

1750. Minimum Length of String After Deleting Similar Ends

Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
The prefix and the suffix should not intersect at any index.
The characters from the prefix and suffix must be the same.
Delete both the prefix and the suffix.
Return the minimum length of s after performing the above operation any number of times (possibly zero times).

 

Example 1:

Input: s = "ca"
Output: 2
Explanation: You can't remove any characters, so the string stays as is.
Example 2:

Input: s = "cabaabac"
Output: 0
Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".
Example 3:

Input: s = "aabccabba"
Output: 3
Explanation: An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".
 

Constraints:

1 <= s.length <= 10^5
s only consists of characters 'a', 'b', and 'c'.
"""


class Solution:
    def minimumLength(self, s: str) -> int:
        """
        >>> s = Solution()
        >>> s.minimumLength("a")
        1
        >>> s.minimumLength("ca")
        2
        >>> s.minimumLength("cabaabac")
        0
        >>> s.minimumLength("aabccabba")
        3
        >>> s.minimumLength("bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb")
        1
        """
        # print(s)
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        if s[0] != s[-1]:
            return len(s)

        i, j, l = 0, -1, len(s)
        while i < l + j and i < l and j >= -l:
            if s[i] != s[j]:
                break

            t = i
            while i < l and s[i] == s[t]:
                i += 1
            if i >= l + j:
                break

            t = j
            while j >= -l and s[j] == s[t]:
                j -= 1

        return l + j - i + 1
