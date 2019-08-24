package main

import "testing"

func equal(a, b []string) bool {
	if len(a) != len(b) {
		return false
	}

	for i, s := range a {
		if s != b[i] {
			return false
		}
	}

	return true
}

func TestTextJustification(t *testing.T) {
	var words []string
	var outputs []string
	var myrst []string

	words = []string{"This", "is", "an", "example", "of", "text", "justification."}
	outputs = []string{"This    is    an", "example  of text", "justification.  "}

	myrst = fullJustify(words, 16)

	if !equal(outputs, myrst) {
		t.Errorf("%q %q %q", words, myrst, outputs)
	}

	words = []string{"What", "must", "be", "acknowledgment", "shall", "be"}
	outputs = []string{"What   must   be", "acknowledgment  ", "shall be        "}
	myrst = fullJustify(words, 16)

	if !equal(outputs, myrst) {
		t.Errorf("%q %q %q", words, myrst, outputs)
	}

	words = []string{"Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"}
	outputs = []string{"Science  is  what we", "understand      well", "enough to explain to", "a  computer.  Art is", "everything  else  we", "do                  "}

	myrst = fullJustify(words, 20)

	if !equal(outputs, myrst) {
		t.Errorf("%q %q %q", words, myrst, outputs)
	}
}
