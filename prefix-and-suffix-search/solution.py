#!/usr/bin/env python3
"""
https://leetcode.cn/problems/prefix-and-suffix-search/

Prefix and Suffix Search

Design a special dictionary that searches the words in it by a prefix and a suffix.

Implement the WordFilter class:

WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string pref, string suff) Returns the index of the word in the dictionary, which has the prefix pref and the suffix suff. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.
 

Example 1:

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]
Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = "e".
 

Constraints:

1 <= words.length <= 10^4
1 <= words[i].length <= 7
1 <= pref.length, suff.length <= 7
words[i], pref and suff consist of lowercase English letters only.
At most 104 calls will be made to the function f.
"""


class Node:
    def __init__(self, v: str):
        self.v: str = v
        self.nextNodes: list[None | Node] = [None] * 26
        self.indices = []

    def __repr__(self):
        return f"{self.v} {self.indices} {[e for e in self.nextNodes if e]}"


class WordFilter:
    def __init__(self, words: list[str]):
        ss = {}
        for i, word in enumerate(words):
            ss[word] = i

        self.root = Node("")
        for word, i in ss.items():
            n = self.root
            for c in word:
                idx = ord(c) - 97
                if n.nextNodes[idx] is None:
                    n.nextNodes[idx] = Node(c)
                node = n.nextNodes[idx]
                node.indices.append(i)
                n = node

        self.reversedRoot = Node("")
        for word, i in ss.items():
            n = self.reversedRoot
            for c in reversed(word):
                idx = ord(c) - 97
                if n.nextNodes[idx] is None:
                    n.nextNodes[idx] = Node(c)
                node = n.nextNodes[idx]
                node.indices.append(i)
                n = node

    def f(self, pref: str, suff: str) -> int:
        n = self.root
        for c in pref:
            idx = ord(c) - 97
            if n.nextNodes[idx] is None:
                return -1
            n = n.nextNodes[idx]
        pIndices = n.indices
        # print(pIndices)

        n = self.reversedRoot
        for c in reversed(suff):
            idx = ord(c) - 97
            if n.nextNodes[idx] is None:
                return -1
            n = n.nextNodes[idx]
        sIndices = n.indices
        # print(sIndices)

        s = set(pIndices).intersection(set(sIndices))
        return max(set(pIndices).intersection(set(sIndices))) if s else -1


def main():
    w = WordFilter(["apple"])
    print(w.root)
    print(w.reversedRoot)
    ans = w.f("a", "e")
    print(ans)


if __name__ == "__main__":
    main()
