package main

import "strconv"

/**
150. Evaluate Reverse Polish Notation
Medium

422

310

Favorite

Share
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
**/

func evalRPN(tokens []string) int {
	var (
		stack = make([]int, len(tokens))
		idx   = 0
		x, y  int
	)

	for _, token := range tokens {
		switch token {
		case "+", "-", "*", "/":
			x, y = stack[idx-2], stack[idx-1]
		default:
			i, _ := strconv.Atoi(token)
			stack[idx] = i
			idx++
			continue
		}

		switch token {
		case "+":
			stack[idx-2] = x + y
		case "-":
			stack[idx-2] = x - y
		case "*":
			stack[idx-2] = x * y
		case "/":
			stack[idx-2] = x / y
		}
		idx--
	}

	return stack[0]
}
