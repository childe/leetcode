#!/usr/bin/env python3

"""
https://leetcode.cn/problems/evaluate-division/
"""


class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors: list[tuple[Node, float]] = []


class Graph:
    def __init__(self):
        self.nodes: dict[str, Node] = {}

    def add_edge(self, a: str, b: str, value: float):
        if a not in self.nodes:
            self.nodes[a] = Node(a)
        if b not in self.nodes:
            self.nodes[b] = Node(b)
        self.nodes[a].neighbors.append((self.nodes[b], value))
        self.nodes[b].neighbors.append((self.nodes[a], 1 / value))

    def find_path(self, a: str, b: str) -> float:
        if a not in self.nodes or b not in self.nodes:
            return -1.0

        visited = set()
        stack = [(self.nodes[a], 1.0)]
        while stack:
            node, value = stack.pop()
            if node.name == b:
                return value
            visited.add(node.name)
            for neighbor, neighbor_value in node.neighbors:
                if neighbor.name not in visited:
                    stack.append((neighbor, value * neighbor_value))
        return -1


class Solution:
    def calcEquation(
        self, equations: list[list[str]], values: list[float], queries: list[list[str]]
    ) -> list[float]:
        graph = Graph()
        for i in range(len(equations)):
            a, b = equations[i]
            value = values[i]
            graph.add_edge(a, b, value)

        rst = []
        for query in queries:
            a, b = query
            rst.append(graph.find_path(a, b))

        return rst


import unittest


class TestSolution(unittest.TestCase):
    def test_calcEquation(self):
        solution = Solution()
        self.assertEqual(
            [6.0, 0.5, -1.0, 1.0, -1.0],
            solution.calcEquation(
                [["a", "b"], ["b", "c"]],
                [2.0, 3.0],
                [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]],
            ),
        )


if __name__ == "__main__":
    unittest.main()
