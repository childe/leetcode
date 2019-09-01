package main

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

func multiply(num1 string, num2 string) (n string) {
	if num1 == "0" || num2 == "0" {
		return "0"
	}

	len1, len2 := len(num1), len(num2)
	r := make([]rune, len1+len2)
	r[0] = '0'

	for i, c1 := range []rune(num1) {
		for j, c2 := range []rune(num2) {
			r[1+i+j] += (c1 - '0') * (c2 - '0')
		}
	}

	for i := len(r) - 1; i > 0; i-- {
		r[i-1] += r[i] / 10
		r[i] = r[i]%10 + '0'
	}

	if r[0] == '0' {
		return string(r[1:])
	}
	return string(r)
}
