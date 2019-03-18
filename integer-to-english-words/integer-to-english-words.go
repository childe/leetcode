package main

import (
	"fmt"
	"strings"
)

/*
https://leetcode.com/problems/integer-to-english-words/

Convert a non-negative integer to its english words representation.
Given input is guaranteed to be less than 2^31 - 1.

Example 1:
Input: 123
Output: "One Hundred Twenty Three"

Example 2:
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
*/

var num_to_word map[int]string = map[int]string{
	0:  "Zero",
	1:  "One",
	2:  "Two",
	3:  "Three",
	4:  "Four",
	5:  "Five",
	6:  "Six",
	7:  "Seven",
	8:  "Eight",
	9:  "Nine",
	10: "Ten",
	11: "Eleven",
	12: "Twelve",
	13: "Thirteen",
	14: "Fourteen",
	15: "Fifteen",
	16: "Sixteen",
	17: "Seventeen",
	18: "Eighteen",
	19: "Nineteen",
	20: "Twenty",
	30: "Thirty",
	40: "Forty",
	50: "Fifty",
	60: "Sixty",
	70: "Seventy",
	80: "Eighty",
	90: "Ninety",
}

func numberToWordsLessThan100(num int) string {
	if num == 0 {
		return ""
	}
	if num < 20 {
		return num_to_word[num]
	}
	if num%10 == 0 {
		return fmt.Sprintf("%s", num_to_word[num/10*10])
	}
	return fmt.Sprintf("%s %s", num_to_word[num/10*10], num_to_word[num%10])
}

func numberToWordsLessThan1000(num int) string {
	if num < 100 {
		return numberToWordsLessThan100(num)
	}

	t := make([]string, 0)
	t = append(t, fmt.Sprintf("%s Hundred", num_to_word[num/100]))
	if num%100 != 0 {
		t = append(t, numberToWordsLessThan100(num%100))
	}
	return strings.Join(t, " ")
}

func numberToWords(num int) string {
	if num == 0 {
		return "Zero"
	}

	t := make([]string, 0)
	words := []string{"Thousand", "Million", "Billion"}
	idx := -1

	for num > 0 {
		w := numberToWordsLessThan1000(num % 1000)
		if w != "" {
			tmp := []string{w}
			if idx >= 0 {
				tmp = append(tmp, words[idx])
			}
			tmp = append(tmp, t...)
			t = tmp
		}
		idx++
		num = num / 1000
	}
	return strings.Trim(strings.Join(t, " "), " ")
}
