#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/string-to-integer-atoi/

Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

spoilers alert... click to show requirements for atoi.

Requirements for atoi:
The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.
"""

import unittest


def initlog(level=None, log="app.log"):
    import logging
    import logging.config
    if level is None:
        level = logging.DEBUG if __debug__ else logging.INFO

    class MyFormatter(logging.Formatter):

        def format(self, record):
            dformatter = '%(levelname)s: [%(asctime)s] - %(pathname)s %(lineno)d - %(message)s'
            formatter = '%(levelname)s: [%(asctime)s] - %(message)s'
            if record.levelno <= logging.DEBUG:
                self._fmt = dformatter
            else:
                self._fmt = formatter
            return super(MyFormatter, self).format(record)

    config = {
        "version": 1,
        "disable_existing_loggers": True,
        "formatters": {
            "custom": {
                '()': MyFormatter
            },
            "simple": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            },
            "verbose": {
                "format": "%(asctime)s - %(levelname)s - %(module)s %(lineno)d - %(message)s"
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "custom",
                "stream": "ext://sys.stdout"
            },
            "file_handler": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "DEBUG",
                "formatter": "custom",
                "filename": log,
                "maxBytes": 10*1000**3,  # 10M
                "backupCount": 5,
                "encoding": "utf8"
            }
        },
        'root': {
            'level': level,
            'handlers': ['file_handler']
        }
    }
    logging.config.dictConfig(config)


INT_MAX = 2147483647
INT_MIN = -2147483648

QUOTIENT = 214748364
REMAINDER_PLUS = 7
REMAINDER_MINUS = 8


class Solution:

    def myAtoi(self, str):
        """
        # @param {string} str
        # @return {integer}
        """

        INT_MAX = 2147483647
        INT_MIN = -2147483648
        QUOTIENT = 214748364
        REMAINDER_PLUS = 7
        REMAINDER_MINUS = 8

        str = str.strip()
        if str == "":
            return 0
        sign = 1
        if str[0] == "-":
            str = str[1:]
            sign = -1
        elif str[0] == "+":
            str = str[1:]
        if str[0] < "0" or str[0] > "9":
            return 0

        r = 0
        for e in str:
            e = ord(e)-48
            if e < 0 or e > 9:
                break
            if sign == 1:
                if r > QUOTIENT or r == QUOTIENT and e > REMAINDER_PLUS:
                    return INT_MAX
            else:
                if r > QUOTIENT or r == QUOTIENT and e > REMAINDER_MINUS:
                    return INT_MIN
            r = r*10+e

        return r*sign


class TestSolution(unittest.TestCase):

    def test_atoi(self):
        import random
        s = Solution()

        self.assertEqual(2147483647, s.myAtoi("2147483647"))
        self.assertEqual(-2147483648, s.myAtoi("-2147483648"))
        self.assertEqual(10, s.myAtoi("10"))
        self.assertEqual(-10, s.myAtoi("-10"))
        self.assertEqual(123, s.myAtoi("123"))
        self.assertEqual(-123, s.myAtoi("-123"))

        self.assertEqual(0, s.myAtoi("-+1"))
        self.assertEqual(0, s.myAtoi("abcd"))
        self.assertEqual(0, s.myAtoi("+++1"))

        for _ in range(100):
            i = random.randint(INT_MIN, INT_MAX)
            self.assertEqual(i, s.myAtoi(str(i)))

        for _ in range(100):
            i = random.randint(INT_MAX+1, 3*INT_MAX)
            self.assertEqual(INT_MAX, s.myAtoi(str(i)))

        for _ in range(100):
            i = random.randint(3*INT_MIN, INT_MIN-1)
            self.assertEqual(INT_MIN, s.myAtoi(str(i)))


def main():
    initlog()
    unittest.main()


if __name__ == '__main__':
    main()
