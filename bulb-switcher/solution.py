#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

'''
https://leetcode.com/problems/bulb-switcher/

There are n bulbs that are initially off.
You first turn on all the bulbs.
Then, you turn off every second bulb.
On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on).
For the nth round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

    Given n = 3.

    At first, the three bulbs are [off, off, off].
    After first round, the three bulbs are [on, on, on].
    After second round, the three bulbs are [on, off, on].
    After third round, the three bulbs are [on, off, off].

    So you should return 1, because there is only one bulb is on.
'''


class Solution(object):

    def bulbSwitch2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0

        import time
        start = time.time()
        count = 0

        bit = 0
        max_num = (1 << n) - 1
        # print 'max_num:',bin(max_num)
        for i in xrange(1, n+1):
            # print 'i:', i
            k = 1 << (i-1)
            # print 'k:', bin(k)
            j = i
            while (j < n):
                k = k << j | k
                j <<= 1
                count += 1
                # print 'k:', bin(k)
            bit ^= k
            # print 'bit:',bin(bit)
            # print
            # if i == 1:
                # print "first rount", (time.time() - start)*n
            # if i == 10:
                # print "10 rount", (time.time() - start)*n/10
            # if i == 100:
                # print "100 rount", (time.time() - start)*n/100
            # if i == 1000:
                # print "1000 rount", (time.time() - start)*n/1000
            # if i == 10000:
                # print "10000 rount", (time.time() - start)*n/10000

        middle = time.time()

        bit &= max_num
        # print 'bit', bin(bit)
        # print 'bit length:', math.log(bit, 2)

        rst = 0
        count2 = 0
        while(bit > 0):
            rst += bit & 1
            bit >>= 1
            count2 += 1

        end = time.time()
        # print 'count', count
        # print 'count2', count2
        #print (middle - start)
        #print (end - middle)

        return rst

    def bulbSwitch3(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0

        import math
        magic_number = int(math.ceil(math.sqrt(n)))
        #print 'magic_number', magic_number
        mask_num = (1 << magic_number)-1
        #print 'mask_num', bin(mask_num)
        magic_cache = [None]*(1+magic_number)

        for i in range(1, 1+magic_number):
            k = 1 << (i-1)
            j = i
            magic_cache[i] = k
            while(j < magic_number):
                magic_cache[i] = magic_cache[i] | (magic_cache[i] << j)
                j <<= 1
            #magic_cache[i] = magic_cache[i] & mask_num

        #for i in range(1, 1+magic_number):
            #print i, bin(magic_cache[i])

        rst = 0
        for i in range((n-1)/magic_number):
            #print 'i:',i,'~'*20
            bit = 0
            # range is (magic_number*i, magic_number*(i+1)]
            for j in range(1+i, 1+magic_number):
                #print 'j:',j
                ##print 'offset:',(magic_number*i)%j
                bit ^= (magic_cache[j] >> ((magic_number*i)%j))
                #print bin(bit)

            bit &= mask_num
            #print 'final bit:',bin(bit)
            while(bit > 0):
                rst += bit & 1
                bit >>= 1

        bit = 0
        #last_range = range(i*magic_number+1,n+1)
        #print 'last range'
        i = (n-1)/magic_number
        #print 'i:',i,'~'*20
        for j in range(1+i, 1+magic_number):
            #print 'j:',j
            #print 'offset:',(magic_number*i)%j
            bit ^= (magic_cache[j] >> ((magic_number*i)%j))
            #print bin(bit)

        mask_num = (1<<(1+(n-1)%magic_number))-1
        #print 'mask_num:',bin(mask_num)
        bit &= mask_num
        #print 'final bit:',bin(bit)
        while(bit > 0):
            rst += bit & 1
            bit >>= 1

        return rst


    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0

        import math
        return int(math.floor(math.sqrt(n)))

class TestSolution(unittest.TestCase):

    def test_bulbSwitch(self):
        import math

        s = Solution()

        for i in range(-100, 1000):
            self.assertEqual(s.bulbSwitch(i), s.bulbSwitch2(i))
        for i in range(1, 1000):
            self.assertEqual(s.bulbSwitch(i), math.floor(math.sqrt(i)))

        my_answer = s.bulbSwitch(0)
        self.assertEqual(0, my_answer)

        my_answer = s.bulbSwitch(1)
        self.assertEqual(1, my_answer)

        my_answer = s.bulbSwitch(3)
        self.assertEqual(1, my_answer)

        my_answer = s.bulbSwitch(10)
        self.assertEqual(3, my_answer)

        my_answer = s.bulbSwitch(100)
        self.assertEqual(10, my_answer)

        my_answer = s.bulbSwitch(100000)
        self.assertEqual(316, my_answer)

if __name__ == '__main__':
    import sys
    if sys.argv[1:]:
        s = Solution()
        print s.bulbSwitch(int(sys.argv[1]))
    else:
        unittest.main()
