package main

import (
	"strings"
)

func outputOneLine(words []string, width int, lastLine bool) string {
	if len(words) == 1 {
		return words[0] + strings.Repeat(" ", width-len(words[0]))
	}

	if lastLine {
		s := strings.Join(words, " ")
		return s + strings.Repeat(" ", width-len(s))
	}

	var (
		gapCount   = len(words) - 1
		spaceCount int
	)

	spaceCount = width
	for _, word := range words {
		spaceCount -= len(word)
	}

	// 如果需要5个空格, 一共三个 Gap(四个 word), 那么前两个 gap 是两个空格, 后面的一个
	div := spaceCount / gapCount
	mod := spaceCount % gapCount

	rst := make([]string, 0, len(words)+spaceCount)

	for i, word := range words[:len(words)-1] {
		rst = append(rst, word)

		rst = append(rst, strings.Repeat(" ", div))
		if i < mod {
			rst = append(rst, " ")
		}
	}

	rst = append(rst, words[len(words)-1])

	return strings.Join(rst, "")
}

func fullJustify(words []string, maxWidth int) []string {
	rst := make([]string, 0)

	var (
		currentLineWitdh = 0
		currentLineWords = make([]string, 0)
	)
	for _, word := range words {
		if currentLineWitdh+len(word)+len(currentLineWords) <= maxWidth {
			currentLineWords = append(currentLineWords, word)
			currentLineWitdh += len(word)
		} else {
			rst = append(rst, outputOneLine(currentLineWords, maxWidth, false))

			currentLineWords = []string{word}
			currentLineWitdh = len(word)
		}
	}

	if len(currentLineWords) > 0 {
		rst = append(rst, outputOneLine(currentLineWords, maxWidth, true))
	}
	return rst
}
