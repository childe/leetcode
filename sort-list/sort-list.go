package main

/**
https://leetcode.com/problems/sort-list/

Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
**/

type ListNode struct {
	Val  int
	Next *ListNode
}

func merge(x, y *ListNode) *ListNode {
	var (
		xPre = &ListNode{0, x}
		head = xPre
	)
	for x != nil && y != nil {
		if y.Val < x.Val {
			//insert
			tmp := y.Next
			y.Next = xPre.Next
			xPre.Next = y
			xPre = y
			y = tmp
		} else {
			xPre = x
			x = x.Next
		}
	}

	if x == nil {
		// insert y
		xPre.Next = y
	}

	if y == nil {

	}

	return head.Next
}

func split(head *ListNode) (*ListNode, *ListNode) {
	if head == nil {
		return nil, nil
	}
	var length = length(head)
	var n = head

	for i := 0; i < (1+length)/2-1; i++ {
		n = n.Next
	}

	nn := n.Next
	n.Next = nil
	return head, nn
}

func length(head *ListNode) int {
	l := 0
	n := head
	for n != nil {
		l++
		n = n.Next
	}
	return l
}

func sortList(head *ListNode) *ListNode {
	if length(head) < 2 {
		return head
	}

	x, y := split(head)
	x = sortList(x)
	y = sortList(y)

	return merge(x, y)
}
