package main

import "testing"

func TestMultiply(t *testing.T) {
	var (
		num1 string
		num2 string

		output string
		myrst  string
	)

	num1 = "0"
	num2 = "0"
	output = "0"

	myrst = multiply(num1, num2)
	if myrst != output {
		t.Errorf("%s %s %s %s %q", num1, num2, output, myrst, myrst)
	}

	num1 = "2"
	num2 = "3"
	output = "6"

	myrst = multiply(num1, num2)
	if myrst != output {
		t.Errorf("%s %s %s %s %q", num1, num2, output, myrst, myrst)
	}

	num1 = "23"
	num2 = "56"
	output = "1288"

	myrst = multiply(num1, num2)
	if myrst != output {
		t.Errorf("%s %s %s %s %q", num1, num2, output, myrst, myrst)
	}

	num1 = "100"
	num2 = "56"
	output = "5600"

	myrst = multiply(num1, num2)
	if myrst != output {
		t.Errorf("%s %s %s %s %q", num1, num2, output, myrst, myrst)
	}

	num1 = "2925"
	num2 = "4787"
	output = "14001975"

	myrst = multiply(num1, num2)
	if myrst != output {
		t.Errorf("%s %s %s %s %q", num1, num2, output, myrst, myrst)
	}

	num1 = "123"
	num2 = "456"
	output = "56088"

	myrst = multiply(num1, num2)
	if myrst != output {
		t.Errorf("%s %s %s %s %q", num1, num2, output, myrst, myrst)
	}

	num1 = "1231231234567888987654566667788"
	num2 = "98765645786970968595678987654345678876543456789"
	output = "121603347995187089387245547846447256361514596486207950723079232688750496212732"
	myrst = multiply(num1, num2)
	if myrst != output {
		t.Errorf("%s %s %s %s %q", num1, num2, output, myrst, myrst)
	}

	num1 = "10000000000000000000000000000001"
	num2 = "10000000000000000000000000000001"
	output = "100000000000000000000000000000020000000000000000000000000000001"

	myrst = multiply(num1, num2)
	if myrst != output {
		t.Errorf("%s %s %s %s %q", num1, num2, output, myrst, myrst)
	}
}

func BenchmarkMultiply_1(b *testing.B) {
	for i := 0; i < b.N; i++ {
		num1 := "123"
		num2 := "456"
		multiply(num1, num2)
	}
}

func BenchmarkMultiply_2(b *testing.B) {
	for i := 0; i < b.N; i++ {
		num1 := "123000000000000000"
		num2 := "456000000000000000"
		multiply(num1, num2)
	}
}

func BenchmarkMultiply_3(b *testing.B) {
	for i := 0; i < b.N; i++ {
		num1 := "1231231234566667788"
		num2 := "9876564578697096859"
		multiply(num1, num2)
	}
}

func BenchmarkMultiply_4(b *testing.B) {
	for i := 0; i < b.N; i++ {
		num1 := "1231231234567888987654566667788"
		num2 := "98765645786970968595678987654345678876543456789"
		multiply(num1, num2)
	}
}
