package main

import "testing"

func TestSolotion(t *testing.T) {
	var answer string

	answer = numberToWords(123)
	if answer != "One Hundred Twenty Three" {
		t.Error(answer)
	}

	answer = numberToWords(3)
	if answer != "Three" {
		t.Error(answer)
	}

	answer = numberToWords(23)
	if answer != "Twenty Three" {
		t.Error(answer)
	}

	answer = numberToWords(20)
	if answer != "Twenty" {
		t.Error(answer)
	}

	answer = numberToWords(200)
	if answer != "Two Hundred" {
		t.Error(answer)
	}

	answer = numberToWords(202)
	if answer != "Two Hundred Two" {
		t.Error(answer)
	}

	answer = numberToWords(12345)
	if answer != "Twelve Thousand Three Hundred Forty Five" {
		t.Error(answer)
	}

	answer = numberToWords(1234567)
	if answer != "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven" {
		t.Error(answer)
	}

	answer = numberToWords(1234567891)
	if answer != "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One" {
		t.Error(answer)
	}
}
