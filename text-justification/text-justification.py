"""
https://leetcode.cn/problems/text-justification/
"""

import unittest


class Solution:
    def fillBlank(self, words: list[str], maxWidth: int, last_line: bool) -> str:
        if last_line or len(words) == 1:
            return " ".join(words).ljust(maxWidth)

        blank_count = maxWidth - sum(len(word) for word in words)
        blank_count_for_each = blank_count // (len(words) - 1)
        blanks = [
            (
                1 + blank_count_for_each
                if i < blank_count % (len(words) - 1)
                else blank_count_for_each
            )
            for i in range(len(words) - 1)
        ]
        ans = ""
        for i, word in enumerate(words[:-1]):
            ans += word
            ans += " " * blanks[i]
        return ans + words[-1]

    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        ans = []
        last_word = 0
        length = len(words[0])
        for i in range(1, len(words)):
            word = words[i]
            if length + 1 + len(word) > maxWidth:
                ans.append(self.fillBlank(words[last_word:i], maxWidth, False))
                last_word = i
                length = len(word)
            else:
                length += 1 + len(word)

        if words[last_word:]:
            ans.append(self.fillBlank(words[last_word:], maxWidth, True))
        return ans


class TestSolution(unittest.TestCase):
    def test_fullJustify(self):
        s = Solution()
        rst = s.fullJustify(
            ["This", "is", "an", "example", "of", "text", "justification."], 16
        )
        self.assertEqual(
            rst, ["This    is    an", "example  of text", "justification.  "]
        )

        rst = s.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16)
        self.assertEqual(
            rst, ["What   must   be", "acknowledgment  ", "shall be        "]
        )
        rst = s.fullJustify(
            [
                "Science",
                "is",
                "what",
                "we",
                "understand",
                "well",
                "enough",
                "to",
                "explain",
                "to",
                "a",
                "computer.",
                "Art",
                "is",
                "everything",
                "else",
                "we",
                "do",
            ],
            20,
        )

        self.assertEqual(
            rst,
            [
                "Science  is  what we",
                "understand      well",
                "enough to explain to",
                "a  computer.  Art is",
                "everything  else  we",
                "do                  ",
            ],
        )


if __name__ == "__main__":
    unittest.main()
