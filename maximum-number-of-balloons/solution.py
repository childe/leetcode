#!
# -*- coding: utf-8 -*-
"""
https://leetcode-cn.com/problems/maximum-number-of-balloons/

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.



Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0


Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
"""

from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        """
        >>> s = Solution()
        >>> s.maxNumberOfBalloons("nlaebolko")
        1
        >>> s.maxNumberOfBalloons("loonbalxballpoon")
        2
        >>> s.maxNumberOfBalloons("leetcode")
        0
        """
        balloon_counter = Counter("balloon")
        text_counter = Counter(text)

        numbers = []
        for c, count in balloon_counter.items():
            numbers.append(text_counter.get(c, 0) // count)

        return min(numbers)
