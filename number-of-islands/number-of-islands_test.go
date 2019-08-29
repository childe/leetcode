package main

import (
	"strings"
	"testing"
)

func TestNumIslands(t *testing.T) {
	var grid [][]byte
	var input string
	var output int
	var myrst int

	input = `
11110
11010
11000
00000
`
	grid = genGrid(input)
	output = 1

	myrst = numIslands(grid)
	if myrst != output {
		t.Errorf("%s\n%d != %d", input, myrst, output)
	}

	input = `
11000
11000
00100
00011
`
	grid = genGrid(input)
	output = 3

	myrst = numIslands(grid)
	if myrst != output {
		t.Errorf("%s\n%d != %d", input, myrst, output)
	}
}

func genGrid(input string) [][]byte {
	grid := make([][]byte, 0)
	input = strings.TrimSpace(input)
	for _, line := range strings.Split(input, "\n") {
		row := make([]byte, len(line))
		for i, b := range line {
			switch b {
			case '0':
				row[i] = '0'
			case '1':
				row[i] = '1'
			}
		}
		grid = append(grid, row)
	}
	return grid
}
