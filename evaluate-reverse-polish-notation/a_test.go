package main

import "testing"

func TestHelloWorld(t *testing.T) {
	// t.Fatal("not implemented")
	var r int
	r = evalRPN([]string{"2", "1", "+", "3", "*"})
	if r != 9 {
		t.Errorf("%d != 9", r)
	}

	r = evalRPN([]string{"4", "13", "5", "/", "+"})
	if r != 6 {
		t.Errorf("%d != 6", r)
	}

	r = evalRPN([]string{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"})
	if r != 22 {
		t.Errorf("%d != 22", r)
	}
}
