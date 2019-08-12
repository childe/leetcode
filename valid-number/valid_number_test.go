package main

import "testing"

var testCases = map[string]bool{
	"0":         true,
	" 0.1 ":     true,
	"abc":       false,
	"1 a":       false,
	"2e10":      true,
	" -90e3   ": true,
	" 1e":       false,
	"e3":        false,
	" 6e-1":     true,
	" 99e2.5 ":  false,
	"53.5e93":   true,
	" --6 ":     false,
	"-+3":       false,
	"95a54e53":  false,
}

func TestValidNumber(t *testing.T) {
	for number, correctAnswer := range testCases {
		rst := isNumber(number)
		if rst != correctAnswer {
			t.Error(number, correctAnswer)
		}
	}
}
