# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/find-and-replace-pattern/description/

You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern.

You may return the answer in any order.



Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.


Note:

1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20
"""


class Solution(object):
    def ifmatch(self, word, pattern):
        d = {}
        for i, letter in enumerate(word):
            if letter not in d:
                d[letter] = pattern[i]
                continue
            if d[letter] != pattern[i]:
                return False
        return True

    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        return [word for word in words if self.ifmatch(word, pattern) and self.ifmatch(pattern, word)]


def main():
    s = Solution()
    print s.findAndReplacePattern(words=["abc", "deq", "mee", "aqq", "dkd", "ccc"], pattern="abb")


if __name__ == '__main__':
    main()
