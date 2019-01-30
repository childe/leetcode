package main

import (
	"strconv"
	"strings"
	"testing"
)

func decode(link string) *ListNode {
	l := strings.Split(link, "->")
	var next, c *ListNode
	for i := len(l) - 1; i >= 0; i-- {
		v, _ := strconv.Atoi(l[i])
		c = &ListNode{
			v,
			nil,
		}
		if next != nil {
			c.Next = next
		}
		next = c
	}

	return c
}

func encode(n *ListNode) string {
	l := make([]string, 0)
	for n != nil {
		l = append(l, strconv.Itoa(n.Val))
		n = n.Next
	}
	return strings.Join(l, "->")
}

func TestSort(t *testing.T) {
	head := decode("4->2->1->3")
	head = sortList(head)
	if encode(head) != "1->2->3->4" {
		t.Error(encode(head))
	}

	head = decode("-1->5->3->4->0")
	head = sortList(head)
	if encode(head) != "-1->0->3->4->5" {
		t.Error(encode(head))
	}

}
func TestMerge(t *testing.T) {
	x := decode("2->4")
	y := decode("1->3")
	head := merge(x, y)
	if encode(head) != "1->2->3->4" {
		t.Error(encode(head))
	}

	// 1 nil
	x = decode("1->2")
	y = nil
	head = merge(x, y)
	if encode(head) != "1->2" {
		t.Error(encode(head))
	}

	// 2 nil
	x = nil
	y = nil
	head = merge(x, y)
	if encode(head) != "" {
		t.Error(encode(head))
	}

	x = decode("1->2")
	y = decode("3->4")
	head = merge(x, y)
	if encode(head) != "1->2->3->4" {
		t.Error(encode(head))
	}

	x = decode("3->4")
	y = decode("1->2")
	head = merge(x, y)
	if encode(head) != "1->2->3->4" {
		t.Error(encode(head))
	}

	x = decode("1->4")
	y = decode("2->3")
	head = merge(x, y)
	if encode(head) != "1->2->3->4" {
		t.Error(encode(head))
	}
}

func TestSplit(t *testing.T) {
	head := decode("4->2->1->3")
	x, y := split(head)
	if encode(x) != "4->2" {
		t.Error(encode(x))
	}
	if encode(y) != "1->3" {
		t.Error(encode(y))
	}

	head = decode("4->2->1")
	x, y = split(head)
	if encode(x) != "4->2" {
		t.Error(encode(x))
	}
	if encode(y) != "1" {
		t.Error(encode(y))
	}

	head = decode("4->2")
	x, y = split(head)
	if encode(x) != "4" {
		t.Error(encode(x))
	}
	if encode(y) != "2" {
		t.Error(encode(y))
	}

	head = decode("4")
	x, y = split(head)
	if encode(x) != "4" {
		t.Error(encode(x))
	}
	if encode(y) != "" {
		t.Error(encode(y))
	}

	x, y = split(nil)
	if encode(x) != "" {
		t.Error(encode(x))
	}
	if encode(y) != "" {
		t.Error(encode(y))
	}
}
