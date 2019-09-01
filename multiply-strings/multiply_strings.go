package main

import (
	"strings"
)

/*
https://leetcode.com/problems/multiply-strings/


Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Note:
1. The length of both num1 and num2 is < 110.
2. Both num1 and num2 contain only digits 0-9.
3. Both num1 and num2 do not contain any leading zero, except the number 0 itself.
4. You must not use any built-in BigInteger library or convert the inputs to integer directly.

*/

func addString(num1 string, num2 string) string {
	if len(num1) > len(num2) {
		return addString(num2, num1)
	}
	rst := make([]byte, len(num2)+1)
	rst[0] = '0'

	var c, c1, c2 byte
	len1, len2 := len(num1), len(num2)
	diff := len2 - len1

	copy(rst[1:], num2[0:diff])

	for i := 0; i < len(num1); i++ {
		c1 = num1[i] - '0'
		c2 = num2[diff+i] - '0'

		c = (c1 + c2)
		rst[diff+i+1] = c + '0'
	}

	for i := len(rst) - 1; i >= 0; i-- {
		if rst[i] > '9' {
			rst[i] -= 10
			rst[i-1] += 1
		}
	}

	if rst[0] == '0' {
		return string(rst[1:])
	}
	return string(rst)
}

type NumZero struct {
	num       string
	zeroCount int
}

func add(n1 NumZero, n2 NumZero) NumZero {
	if n1.num == "0" {
		return n2
	}
	if n2.num == "0" {
		return n1
	}

	if n1.zeroCount > n2.zeroCount {
		return add(n2, n1)
	}

	s := addString(n1.num, n2.num+strings.Repeat("0", n2.zeroCount-n1.zeroCount))
	return NumZero{s, n1.zeroCount}
}

func multiply(num1 string, num2 string) (n string) {
	if len(num1) > len(num2) {
		return multiply(num2, num1)
	}

	if num1 == "0" || num1 == "" {
		return "0"
	}

	if len(num1) == 1 {
		n = num2
		for i := 1; i < int(num1[0])-'0'; i++ {
			n = addString(n, num2)
		}
		return
	}

	len1, len2 := len(num1), len(num2)
	p1 := NumZero{multiply(num1[0:len1/2], num2[len2/2:]), len1 - len1/2}
	p2 := NumZero{multiply(num1[len1/2:], num2[0:len2/2]), len2 - len2/2}
	rst := add(p1, p2)
	rst = add(rst, NumZero{multiply(num1[0:len1/2], num2[0:len2/2]), len1 + len2 - len1/2 - len2/2})
	rst = add(rst, NumZero{multiply(num1[len1/2:], num2[len2/2:]), 0})

	return rst.num + strings.Repeat("0", rst.zeroCount)
}

func atoi(s string) (n int) {
	for _, c := range s {
		n = 10*n + int(c) - '0'
	}
	return
}

func iaoi(n int) string {
	rst := make([]byte, 0)
	for n > 0 {
		rst = append(rst, byte(n%10+'0'))
		n = n / 10
	}
	return string(rst)
}
