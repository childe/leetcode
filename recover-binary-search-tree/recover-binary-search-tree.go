/**
https://leetcode.com/problems/recover-binary-search-tree/
**/

package main

import "fmt"

// TreeNode is tree node
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func ifValid(root *TreeNode) (valid bool, small, large *TreeNode) {
	var smallL, largeL, smallR, largeR *TreeNode
	var validL, validR bool

	if root.Left != nil {
		validL, smallL, largeL = ifValid(root.Left)
		if !validL {
			return false, nil, nil
		}

		if root.Val < largeL.Val {
			return false, nil, nil
		}
	}

	if root.Right != nil {
		validR, smallR, largeR = ifValid(root.Right)
		if !validR {
			return false, nil, nil
		}

		if root.Val > smallR.Val {
			return false, nil, nil
		}
	}

	if root.Left == nil {
		smallL = root
	}
	if root.Right == nil {
		largeR = root
	}
	return true, smallL, largeR
}

func deserialize(l []interface{}) (root *TreeNode) {
	if len(l) == 0 || l[0] == nil {
		return nil
	}

	var current, last *TreeNode

	root = &TreeNode{l[0].(int), nil, nil}
	current, last = root, root
	var left bool = true

	for _, i := range l[1:] {
		//fmt.Println(i)
		var n, next *TreeNode
		if i != nil {
			n = &TreeNode{i.(int), nil, nil}
		}

		if left {
			current.Left = n
		} else {
			next = current.Right
			current.Right = n

			if last == current {
				current = n
			} else {
				current = next
			}
		}
		left = !left

		if n != nil {
			last.Right = n
			last = n
		}
	}

	for current != nil {
		next := current.Right
		current.Right = nil
		current = next
	}
	return
}

func serialize(root *TreeNode) (rst []interface{}) {
	if root == nil {
		return nil
	}

	rst = make([]interface{}, 0)

	stack := []*TreeNode{root}
	for len(stack) > 0 {
		c := stack[0]
		stack = stack[1:]
		if c == nil {
			rst = append(rst, nil)
		} else {
			rst = append(rst, c.Val)
			stack = append(stack, c.Left)
			stack = append(stack, c.Right)
		}
	}

	for i := len(rst) - 1; i >= 0; i-- {
		if rst[i] != nil {
			rst = rst[:i+1]
			return
		}
	}
	return
}

func findMostLeft(n *TreeNode) *TreeNode {
	if n.Left == nil {
		return nil
	}

	r := n.Left

	for r.Right != nil && r.Right != n {
		r = r.Right
	}

	return r
}

func findMostRight(n *TreeNode) *TreeNode {
	if n.Right == nil {
		return nil
	}

	if findMostLeft(n.Right) == n {
		return n.Right
	}

	r := n.Right
	for r.Left != nil {
		if r == n {
			return n.Right
		}
		r = r.Left
	}
	return r
}

func f(current, preNode *TreeNode, firstNodeExist, debug bool) (rst bool) {
	var print func(format string, a ...interface{}) (n int, err error)
	if debug {
		print = fmt.Printf
	} else {
		print = func(format string, a ...interface{}) (n int, err error) {
			return 0, nil
		}
	}

	defer func() {
		if rst {
			if !firstNodeExist {
				print("first: %d\n", current.Val)
			} else {
				print("second: %d\n", current.Val)
			}
		}
	}()

	print("current: %d\n", current.Val)
	if !firstNodeExist {
		mostRight := findMostRight(current)
		print("mostRight: %d\n", mostRight.Val)
		if mostRight == current || mostRight == nil {
			mostRight = current.Right
		}
		if current.Val > mostRight.Val {
			return true
		}
	} else {
		print("pre: %d\n", preNode.Val)
		if current.Val < preNode.Val {
			return true
		}
	}
	return false
}

func traverseTree(root *TreeNode, f func(current, preNode *TreeNode, firstNodeExist, debug bool) bool, debug bool) {
	var firstNode *TreeNode
	var secondNode *TreeNode

	var preNode *TreeNode
	var current = root
	for current != nil {
		mostLeft := findMostLeft(current)

		if mostLeft == nil || mostLeft.Right == current {
			if f(current, preNode, firstNode != nil, debug) {
				if firstNode == nil {
					firstNode = current
				} else {
					secondNode = current
				}
			}

			preNode = current
			current = current.Right

			if mostLeft != nil {
				mostLeft.Right = nil
			}
		} else {
			mostLeft.Right = current
			current = current.Left
		}
	}

	firstNode.Val, secondNode.Val = secondNode.Val, firstNode.Val
}

func recoverTree(root *TreeNode) {
	debug := false
	traverseTree(root, f, debug)
}

func main() {
	var l []interface{}
	var root *TreeNode
	var valid bool

	l = []interface{}{1, 3, nil, nil, 2}
	root = deserialize(l)
	recoverTree(root)
	fmt.Println(serialize(root))
	valid, _, _ = ifValid(root)
	fmt.Println(valid)

	l = []interface{}{1, 2, nil, 3}
	root = deserialize(l)
	recoverTree(root)
	fmt.Println(serialize(root))
	valid, _, _ = ifValid(root)
	fmt.Println(valid)

	l = []interface{}{3, 1, 4, nil, nil, 2}
	root = deserialize(l)
	recoverTree(root)
	fmt.Println(serialize(root))
	valid, _, _ = ifValid(root)
	fmt.Println(valid)

	l = []interface{}{2, nil, 4, 3, nil, 1}
	root = deserialize(l)
	recoverTree(root)
	fmt.Println(serialize(root))
	valid, _, _ = ifValid(root)
	fmt.Println(valid)

	l = []interface{}{68, 41, nil, -85, nil, -73, -49, -98, nil, nil, nil, -124}
	root = deserialize(l)
	recoverTree(root)
	fmt.Println(serialize(root))
	valid, _, _ = ifValid(root)
	fmt.Println(valid)

	l = []interface{}{3, 4, nil, 1, nil, nil, 2}
	root = deserialize(l)
	recoverTree(root)
	fmt.Println(serialize(root))
	valid, _, _ = ifValid(root)
	fmt.Println(valid)
}
