package main

import "testing"

func TestMultiply(t *testing.T) {
	var (
		num1 string
		num2 string

		output string
		myrst  string
	)

	num1 = "2"
	num2 = "3"
	output = "6"

	myrst = multiply(num1, num2)
	if myrst != output {
		t.Errorf("%s %s %s %s", num1, num2, output, myrst)
	}

	num1 = "123"
	num2 = "456"
	output = "56088"

	myrst = multiply(num1, num2)
	if myrst != output {
		t.Errorf("%s %s %s %s", num1, num2, output, myrst)
	}
}
