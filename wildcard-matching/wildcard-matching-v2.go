package main

import (
	"flag"
	"fmt"

	"github.com/golang/glog"
)

/*
https://leetcode.com/problems/wildcard-matching/

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:
Input:
s = "acdcb"
p = "a*c?b"
Output: false
*/

func isMatch(s string, p string) bool {
	s = "^" + s
	p = "^" + p
	var (
		spos      int
		ppos      int
		slen      = len(s)
		plen      = len(p)
		pposarray = make([]int, len(p))
		backtrack bool
	)

	for i := range pposarray {
		pposarray[i] = slen
	}

	for {
		backtrack = false
		for !backtrack {
			glog.Infof("%d %d %v %s %s\n", spos, ppos, pposarray[:ppos], s[:spos], p[:ppos])
			switch {
			case spos > slen || ppos > plen:
				panic("outofindex")
			case spos == slen && ppos == plen:
				return true
			case ppos == plen:
				backtrack = true
			case spos == slen:
				if p[ppos] != '*' {
					backtrack = true
				} else {
					pposarray[ppos] = slen - 1
					ppos++
				}

			case p[ppos] == '*':
				spos = pposarray[ppos]
				pposarray[ppos]--
				ppos++
			case p[ppos] == '?':
				pposarray[ppos] = spos
				spos++
				ppos++
			default:
				if p[ppos] == s[spos] {
					pposarray[ppos] = spos
					ppos++
					spos++
				} else {
					backtrack = true
				}
			}
		}

		// backtrack
		glog.Infof("%d %d %v %s %s\n", spos, ppos, pposarray[:ppos], s[:spos], p[:ppos])

		ppos--
		spos = pposarray[ppos]

		for ppos > 0 && spos > 0 {
			if p[ppos] == '*' && pposarray[ppos] != pposarray[ppos-1] {
				spos = pposarray[ppos]
				pposarray[ppos]--
				ppos++
				break
			}
			ppos--
			spos = pposarray[ppos]
		}

		glog.Infof("%d %d %v\n", spos, ppos, pposarray)
		if ppos <= 0 || spos <= 0 {
			return false
		}
		glog.Infof("%d %d %v %s %s\n", spos, ppos, pposarray[:ppos], s[:spos], p[:ppos])
	}

	return false
}

func main() {
	flag.Parse()

	var s, p string
	var r bool

	s = ""
	p = ""
	r = isMatch(s, p)
	fmt.Println(r == true)

	s = ""
	p = "*"
	r = isMatch(s, p)
	fmt.Println(r == true)

	s = ""
	p = "?"
	r = isMatch(s, p)
	fmt.Println(r == false)

	s = ""
	p = "a"
	r = isMatch(s, p)
	fmt.Println(r == false)

	s = "aa"
	p = "a"
	r = isMatch(s, p)
	fmt.Println(r == false)

	s = "aa"
	p = "*"
	r = isMatch(s, p)
	fmt.Println(r == true)

	s = "bc"
	p = "*a"
	r = isMatch(s, p)
	fmt.Println(r == false)

	s = "adceb"
	p = "*a*b"
	r = isMatch(s, p)
	fmt.Println(r == true)

	s = "ab"
	p = "*?*?*"
	r = isMatch(s, p)
	fmt.Println(r == true)

	s = "acdcb"
	p = "a*c?b"
	r = isMatch(s, p)
	fmt.Println(r == false)

	s = "abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb"
	p = "*aa*ba*a*bb*aa*ab*a*aaaaaa*a*aaaa*bbabb*b*b*aaaaaaaaa*a*ba*bbb*a*ba*bb*bb*a*b*bb"
	r = isMatch(s, p)
	fmt.Println(r == false)

	glog.Flush()
}
