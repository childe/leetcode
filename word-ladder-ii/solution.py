# -*- coding: utf-8 -*-

import time

"""
https://leetcode-cn.com/problems/word-ladder-ii/

给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换后得到的单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if len(beginWord) != len(endWord):
            return []

        # self.diffCache = {}
        self.diffTime = 0

        wordList = [w for w in wordList if len(w) == len(beginWord)]
        s = time.time()
        self.relations = self.createRelations(wordList + [beginWord])
        # print("createRelations", time.time() - s)
        # print("relations", self.relations)

        leftSet = set([beginWord])
        rightSet = set(wordList)
        rightSet.difference_update(leftSet)
        # levelSet = [set([beginWord])]
        nextWords = {}  # word -> []

        # path , step
        # s = [(beginWord,)]
        # visited = {}  # step -> words
        # cache = {}
        # rst = []

        midSet = set([beginWord])
        level = 0
        while midSet and endWord not in midSet:
            level += 1
            # print("level", level)
            # print("word length", len(midSet))
            s = time.time()
            nextMidSet = set()
            for w in midSet:
                _nextWords = self.findNextWords(rightSet, w)
                # rightSet.difference_update(_nextWords)
                nextMidSet.update(_nextWords)
                nextWords[w] = _nextWords
            midSet = nextMidSet
            # print("time", time.time() - s)

            if endWord in midSet:
                # print("nextWords", nextWords)
                rst = self.buildResult(beginWord, endWord, nextWords)
                break
            if not midSet:
                # print("nextWords", nextWords)
                rst = []
                break

            rightSet.difference_update(midSet)
            leftSet.update(midSet)

        # print("nextWords", nextWords)
        # return self.buildResult(beginWord, nextWords)
        # print("diff time", self.diffTime)
        return rst

    def findNextWords(self, rightSet, word):
        # hit = cache.get(word)
        # if hit is not None:
        # print("hit")
        # return hit

        # print("findNextWords", word, leftSet)

        words = [w for w in self.relations.get(word, []) if w in rightSet]
        return words
        return [w for w in rightSet if self.diff(word, w) == 1]

        # cache[word] = words
        # return words

    def buildResult(self, beginWord, endWord, nextWords):
        # count = 0
        currentSet = [(beginWord,)]
        nextSet = []
        while True:
            for path in currentSet:
                lastWord = path[-1]
                for n in nextWords.get(lastWord, []):
                    # count += 1
                    nextSet.append(path + (n,))

            if not nextSet:
                # print("count", count)
                return [p for p in currentSet if endWord == p[-1]]
            currentSet = nextSet
            nextSet = []

    def createRelations(self, wordList):
        buckets = {}
        for w in wordList:
            for i, c in enumerate(w):
                key = w[:i] + "_" + w[i + 1 :]
                buckets.setdefault(key, set())
                buckets[key].add(w)

        # print("buckets", buckets)
        relations = {}
        for v in buckets.values():
            for w in v:
                relations.setdefault(w, set())
                relations[w].update(v)
                relations[w].remove(w)
        return relations

        relations = {}
        for w in wordList:
            relations.setdefault(w, set())
        for w1 in wordList:
            for w2 in wordList:
                if self.diff(w1, w2) == 1:
                    relations[w1].add(w2)
                    relations[w2].add(w1)
        return relations

    def diff(self, w1, w2):
        s = time.time()
        d = 0
        for i, c in enumerate(w1):
            if c != w2[i]:
                d += 1
                if d > 1:
                    break

        self.diffTime += time.time() - s
        return d

        return sum([e[0] != e[1] for e in zip(w1, w2)])
        if (w1, w2) in self.diffCache:
            return self.diffCache[(w1, w2)]
        if (w2, w1) in self.diffCache:
            return self.diffCache[(w2, w1)]
        diff = sum([e[0] != e[1] for e in zip(w1, w2)])
        self.diffCache[(w1, w2)] = diff
        self.diffCache[(w2, w1)] = diff
        return diff


def main():
    s = Solution()

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    ans = s.findLadders(beginWord, endWord, wordList)
    print(ans)
    assert set(ans) == set(
        [("hit", "hot", "dot", "dog", "cog"), ("hit", "hot", "lot", "log", "cog"),]
    )
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    ans = s.findLadders(beginWord, endWord, wordList)
    print(ans)
    assert ans == []

    beginWord = "a"
    endWord = "c"
    wordList = ["a", "b", "c"]
    ans = s.findLadders(beginWord, endWord, wordList)
    print(ans)
    assert ans == [("a", "c")]

    beginWord = "talk"
    endWord = "tail"
    wordList = ["talk", "tons", "fall", "tail", "gale", "hall", "negs"]
    ans = s.findLadders(beginWord, endWord, wordList)
    print(ans)
    assert ans == []

    lines = open("./input.txt").readlines()
    for group in list(zip(*[iter(lines)] * 3)):
        beginWord = group[0].strip().strip('"')
        lastWord = group[1].strip().strip('"')
        wordList = [e.strip('"') for e in group[2].strip()[1:-1].split(",")]
        ans = s.findLadders(beginWord, lastWord, wordList)
        print(len(ans))


if __name__ == "__main__":
    main()
