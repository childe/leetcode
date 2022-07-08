#!/usr/bin/env python3
"""
https://leetcode.cn/problems/replace-words/

In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.

 

Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
 

Constraints:

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 10^6
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Every two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.
"""


class Node(object):
    def __init__(self, x):
        self.val: str = x
        self.nextNodes: list[Node | None] = [None] * 26
        self.isLeaf: bool = False

    def __repr__(self):
        return self.val


class Solution:
    def findRoot(self, word: str) -> str:
        root = ""
        n = self.root
        # print(n.val, n.nextNodes, n.isLeaf)
        for c in word:
            # idx = ord(c) - 97
            # print(idx)
            if n.isLeaf:
                return root
            if n.nextNodes[ord(c) - 97] is None:
                return ""
            root += c
            n = n.nextNodes[ord(c) - 97]

        return ""

    def initTree(self, dictionary: list[str]):
        self.root = Node("")
        for word in dictionary:
            n = self.root
            for c in word:
                idx = ord(c) - 97
                if n.nextNodes[idx] is not None:
                    n = n.nextNodes[idx]
                    continue
                nNode = Node(c)
                n.nextNodes[idx] = nNode
                # print(n.val, n.nextNodes)
                n = nNode
            n.isLeaf = True

    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        """
        >>> s = Solution()
        >>> s.replaceWords(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery")
        'the cat was rat by the bat'
        >>> s.replaceWords(dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs")
        'a a b c'
        >>> s.replaceWords(["a", "aa", "aaa", "aaaa"], "aaaa")
        'a'
        """
        self.initTree(dictionary)
        ans = []
        for word in sentence.split():
            root = self.findRoot(word)
            if root:
                ans.append(root)
            else:
                ans.append(word)

        return " ".join(ans)


s = Solution()
s.replaceWords(
    dictionary=["cat", "bat", "rat"], sentence="the cattle was rattled by the battery"
)
