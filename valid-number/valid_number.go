package main

import (
	"strings"
)

/*
Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.
*/

func isInteger(s string) bool {
	var hasDigit = false
	for i, c := range s {
		switch {
		case c >= '0' && c <= '9':
			hasDigit = true
		case c == '-' || c == '+':
			if i > 0 {
				return false
			}
		default:
			return false
		}
	}
	return hasDigit
}

func isIntegerOrFloat(s string) bool {
	var hasDot = false
	var hasDigit = false
	for i, c := range s {
		switch {
		case c >= '0' && c <= '9':
			hasDigit = true
		case c == '-' || c == '+':
			if i > 0 {
				return false
			}
		case c == '.':
			if hasDot {
				return false
			}
			hasDot = true
		default:
			return false
		}
	}

	return hasDigit
}

func isNumber(s string) bool {
	s = strings.TrimSpace(s)
	for i, c := range s {
		if c == 'e' || c == 'E' {
			return isIntegerOrFloat(s[:i]) && isInteger(s[i+1:])
		}
	}
	return isIntegerOrFloat(s)
}
