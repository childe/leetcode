#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/clone-graph/description/


Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None
        head = node.label

        allNodes = dict()
        visited = set()

        from collections import deque
        stack = deque([node])
        visited.add(node.label)
        while stack:
            # print 'stack', [e.label for e in list(stack)]
            # print 'allNodes', allNodes.keys()
            node = stack.popleft()
            # print 'node', node.label
            # print 'neighbors', [e.label for e in node.neighbors]
            # print

            new_node = allNodes.get(node.label, UndirectedGraphNode(node.label))
            allNodes.setdefault(node.label, new_node)
            for n in node.neighbors:
                if n.label not in visited:
                    visited.add(n.label)
                    stack.append(n)
                the_neighbor = allNodes.get(n.label, UndirectedGraphNode(n.label))
                allNodes.setdefault(the_neighbor.label, the_neighbor)
                new_node.neighbors.append(the_neighbor)

        return allNodes[head]


def createGraph(s):
    """
    s is like {0,1,5#1,2,5#2,3#3,4,4#4,5,5#5}
    type s: string
    rtype: UndirectedGraphNode
    """
    s = s[1:-1]
    allNodes = {}
    for line in s.split('#'):
        labels = line.split(',')
        label = labels[0]
        node = allNodes.get(label, UndirectedGraphNode(label))
        allNodes.setdefault(label, node)
        for label in labels[1:]:
            neighbor = allNodes.get(label, UndirectedGraphNode(label))
            allNodes.setdefault(label, neighbor)
            node.neighbors.append(neighbor)

    return allNodes[s.split(',', 1)[0]]


def graphToString(node):
    """
    type s: UndirectedGraphNode
    rtype: string
    """
    stack = [node]
    visited = set()
    allNodes = []
    while stack:
        node = stack.pop()
        allNodes.append((node.label, node.neighbors))
        for neighbor in node.neighbors:
            if neighbor.label not in visited:
                stack.insert(0, neighbor)
                visited.add(neighbor.label)
    allNodes.sort(key=lambda x: x[0])
    lines = []
    for node, neighbors in allNodes:
        line = [node]
        line.extend([e.label for e in neighbors])
        lines.append(line)
    return '{' + '#'.join([','.join(line) for line in lines]) + '}'


def main():
    s = Solution()

    import sys
    # graph = createGraph('{0,1,5#1,2,5#2,3#3,4,4#4,5,5#5}')

    graph = createGraph(sys.argv[1])
    rst = graphToString(graph)
    print rst
    print rst == sys.argv[1]

    new_graph = s.cloneGraph(graph)
    rst = graphToString(new_graph)
    print rst
    print rst == sys.argv[1]


if __name__ == '__main__':
    main()
