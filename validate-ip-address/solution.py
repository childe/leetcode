#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
https://leetcode.com/problems/validate-ip-address/description/

Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:
Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".

Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".

Example 3:
Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.
'''


class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if IP == '':
            return 'Neither'

        IP = IP.upper()

        if self.validIPV4(IP):
            return 'IPv4'
        if self.validIPV6(IP):
            return 'IPv6'

        return 'Neither'

    def validIPV4(self, IP):
        """
        :type IP: str
        :rtype: bool
        >>> s = Solution()
        >>> s.validIPV4("172.16.254.1")
        True
        >>> s.validIPV4("2001:0DB8:85A3:0:0:8A2E:0370:7334")
        False
        >>> s.validIPV4("256.256.256.256")
        False
        >>> s.validIPV4("1.1.1.01")
        False
        >>> s.validIPV4("1.0.1.")
        False
        """
        if IP[0] == '0':
            return False
        splited = IP.split('.')
        if len(splited) != 4:
            return False
        for e in splited:
            if not e:
                return False
            if e == '0':
                continue
            if e[0] == '0':
                return False
            if not e.isdigit():
                return False
            if not 0 <= int(e) <= 255:
                return False
        return True

    def validIPV6(self, IP):
        """
        :type IP: str
        :rtype: bool
        >>> s = Solution()
        >>> s.validIPV6("172.16.254.1")
        False
        >>> s.validIPV6("2001:0DB8:85A3:0:0:8A2E:0370:7334")
        True
        >>> s.validIPV6("256.256.256.256")
        False
        >>> s.validIPV6("2001:db8:85a3:0::8a2E:0370:7334")
        False
        """

        splited = IP.split(':')
        if len(splited) != 8:
            return False
        for e in splited:
            if not 0 < len(e) <= 4:
                return False
            if any([c not in 'ABCDEF0123456789' for c in e]):
                return False
        return True
