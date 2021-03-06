#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/add-and-search-word-data-structure-design/description/

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or `.`. A `.` means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""


class C(object):
    def __init__(self, leaf=False):
        self.children = dict()
        self.leaf = leaf


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = C()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        >>> w = WordDictionary()
        >>> w.addWord('ran')
        >>> w.root.children['r'].children['a'].leaf
        False
        >>> w.root.children['r'].children['a'].children['n'].leaf
        True
        >>> w.addWord('rune')
        >>> w.root.children['r'].children['u'].children['n'].children.keys()
        ['e']
        >>> w = WordDictionary()
        >>> w.addWord('a')
        >>> w.addWord('ab')
        >>> w.root.children['a'].leaf
        True
        >>> len(w.root.children['a'].children)
        1
        >>> w = WordDictionary()
        >>> w.addWord('abcd')
        >>> sorted(w.root.children.keys())
        ['a']
        >>> w.addWord('abxy')
        >>> sorted(w.root.children.keys())
        ['a']
        >>> len(w.root.children['a'].children['b'].children)
        2
        """
        current = self.root
        for c in word:
            child = current.children.get(c)
            if child:
                current = child
            else:
                child = C()
                current.children[c], current = child, child
        current.leaf = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool

        >>> w = WordDictionary()
        >>> w.addWord('abcd')
        >>> w.search('abcd')
        True
        >>> w.search('ab')
        False
        >>> w.search('abcdxy')
        False
        """

        stack = [(self.root, -1)]
        lastP = len(word)-1
        while stack:
            node, pos = stack.pop()
            # print node.char, pos, len(stack)

            if pos == lastP:
                if node.leaf:
                    return True
                continue

            c = word[pos+1]
            # print 'char is', c
            if c == '.':
                for child in node.children.values():
                    stack.append((child, pos+1))
            else:
                child = node.children.get(c)
                if child is not None:
                    stack.append((child, pos+1))

        return False


def main():
    w = WordDictionary()
    w.addWord('ran')
    w.addWord('rune')
    print w.search('r.n')


if __name__ == '__main__':
    main()
