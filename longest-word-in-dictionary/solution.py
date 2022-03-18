#!/usr/bin/env python3

"""
https://leetcode-cn.com/problems/longest-word-in-dictionary/solution/

Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.



Example 1:

Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:

Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".


Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 30
words[i] consists of lowercase English letters.

"""


class Solution:
    def longestWord(self, words: list[str]) -> str:
        """
        >>> s = Solution()
        >>> s.longestWord(["w","wo","wor","worl","world"])
        'world'
        >>> s.longestWord(["a","banana","app","appl","ap","apply","apple"])
        'apple'
        """
        N = 1000 * 30 + 1
        trie_table = [[0] * 26 for _ in range(N)]
        index = 0
        for word in words:
            p = 0
            for c in word[:-1]:
                col = ord(c) - ord("a")
                if trie_table[p][col] == 0:
                    index += 1
                    trie_table[p][col] = index
                p = abs(trie_table[p][col])

            col = ord(word[-1]) - ord("a")
            if trie_table[p][col] == 0:
                index += 1
                trie_table[p][col] = -index
            elif trie_table[p][col] > 0:
                trie_table[p][col] *= -1

        def has_prefix(prefix):
            p = 0
            for c in prefix[:-1]:
                p = abs(trie_table[p][ord(c) - ord("a")])
                if p == 0:
                    return False
            return trie_table[p][ord(prefix[-1]) - ord("a")] < 0

        ans = ""
        for w in set(words):
            if len(w) < len(ans):
                continue
            if len(w) == len(ans) and ans <= w:
                continue
            for i in range(1, 1 + len(w)):
                if not has_prefix(w[:i]):
                    break
            else:
                ans = w
        return ans
