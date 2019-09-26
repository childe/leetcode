# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/explore/learn/card/queue-stack/219/stack-and-dfs/884/
"""
# Definition for a Node.


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

    def __str__(self):
        return '{}'.format(self.val)


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        s = [node]
        visited = {}

        while s:
            n = s.pop()
            # print(n.val, ','.join([str(e) for e in n.neighbors]))
            new_n = Node(n.val, [])
            visited[n] = new_n

            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = None
                    s.append(neighbor)

        s = [node]
        v = set([node])
        while s:
            n = s.pop()
            # print(n.val, ','.join([str(e) for e in n.neighbors]))
            new_n = visited[n]

            for neighbor in n.neighbors:
                new_n.neighbors.append(visited[neighbor])
                if neighbor not in v:
                    v.add(neighbor)
                    s.append(neighbor)

        return visited[node]


def main():
    s = Solution()

    nodes = []
    for i in range(1, 5):
        nodes.append(Node(i, []))

    neighbors = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [2, 0]}
    for o, ns in neighbors.items():
        for n in ns:
            nodes[o].neighbors.append(nodes[n])

    head = s.cloneGraph(nodes[0])

    n = head
    print(n.val, ','.join([str(e) for e in n.neighbors]))

    n = head.neighbors[0]
    print(n.val, ','.join([str(e) for e in n.neighbors]))

    n = head.neighbors[1]
    print(n.val, ','.join([str(e) for e in n.neighbors]))

    n = n.neighbors[1]
    print(n.val, ','.join([str(e) for e in n.neighbors]))


if __name__ == '__main__':
    main()
