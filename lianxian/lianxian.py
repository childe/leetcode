#!/usr/bin/env python


class Point(object):
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x

    def __repr__(self):
        return f"({self.y}, {self.x})"


class Line(object):
    def __init__(self, points: list[Point]):
        self.points = points

    def __repr__(self):
        return f"{self.points}"


def get_right_candidates(matrix: list[list[int]], x: int, y: int) -> list[list[Point]]:
    """
    获取右边的候选点
    >>> matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    >>> get_right_candidates(matrix, 0, 0)
    [[(0, 0), (0, 1)], [(0, 0), (0, 1), (0, 2)]]
    >>> matrix = [[1, 0, 1], [1, 1, 1], [1, 1, 1]]
    >>> get_right_candidates(matrix, 0, 0)
    []
    """
    until = x
    for i in range(x + 1, len(matrix[0])):
        v = matrix[y][i]
        # print(f"{i=} {v=}")
        if v == 0:
            until = i
            break
    else:
        until = len(matrix[0])

    # print(f"{until=}")
    candidates = [[Point(y, x)]]
    for i in range(x + 1, until):
        candidates.append(candidates[-1] + [Point(y, i)])
    return candidates[1:]


def get_down_candidates(matrix: list[list[int]], x: int, y: int) -> list[list[Point]]:
    """
    获取下边的候选点
    >>> matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    >>> get_down_candidates(matrix, 0, 0)
    [[(0, 0), (1, 0)], [(0, 0), (1, 0), (2, 0)]]
    >>> matrix = [[1, 1, 1], [0, 1, 1], [1, 1, 1]]
    >>> get_down_candidates(matrix, 0, 0)
    []
    """
    until = x
    for i in range(y + 1, len(matrix)):
        v = matrix[i][x]
        # print(f"{i=} {v=}")
        if v == 0:
            until = i
            break
    else:
        until = len(matrix)

    # print(f"{until=}")

    candidates = [[Point(y, x)]]
    for i in range(y + 1, until):
        candidates.append(candidates[-1] + [Point(i, x)])
    return candidates[1:]


def get_right_down_candidates(
    matrix: list[list[int]], x: int, y: int
) -> list[list[Point]]:
    """
    获取右下边的候选点
    >>> matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    >>> get_right_down_candidates(matrix, 0, 0)
    [[(0, 0), (1, 1)], [(0, 0), (1, 1), (2, 2)]]
    >>> matrix = [[1, 1, 1], [1, 1, 1], [1, 0, 0]]
    >>> get_right_down_candidates(matrix, 0, 0)
    [[(0, 0), (1, 1)]]
    >>> matrix=[[0, 1, 0]]
    >>> get_right_down_candidates(matrix, 1, 0)
    []
    """
    i, j, c = x, y, 0
    while i < len(matrix[0]) and j < len(matrix):
        v = matrix[j][i]
        # print(f"{i=} {j=} {v=}")
        if v == 0:
            break
        else:
            i += 1
            j += 1
            c += 1

    # print(f"{c=}")

    candidates = [[Point(y, x)]]
    for o in range(1, c):
        candidates.append(candidates[-1] + [Point(y + o, x + o)])
    return candidates[1:]


def get_left_down_candidates(
    matrix: list[list[int]], x: int, y: int
) -> list[list[Point]]:
    """
    获取右下边的候选点
    >>> matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    >>> get_left_down_candidates(matrix, 2, 0)
    [[(0, 2), (1, 1)], [(0, 2), (1, 1), (2, 0)]]
    >>> matrix = [[1, 1, 1], [1, 1, 1], [0, 0, 0]]
    >>> get_left_down_candidates(matrix, 2, 0)
    [[(0, 2), (1, 1)]]
    >>> matrix=[[0, 1, 0]]
    >>> get_left_down_candidates(matrix, 1, 0)
    []
    """
    i, j, c = x, y, 0
    while i >= 0 and j < len(matrix):
        v = matrix[j][i]
        # print(f"{i=} {j=} {v=}")
        if v == 0:
            break
        else:
            i -= 1
            j += 1
            c += 1

    # print(f"{c=}")

    candidates = [[Point(y, x)]]
    for o in range(1, c):
        candidates.append(candidates[-1] + [Point(y + o, x - o)])
    return candidates[1:]


def find_all_candidates(matrix: list[list[int]]) -> list[list[Point]]:
    candidates = []
    for y, row in enumerate(matrix):
        for x, v in enumerate(row):
            if v == 1:
                candidates.append([Point(y, x)])
                candidates.extend(get_right_candidates(matrix, x, y))
                candidates.extend(get_down_candidates(matrix, x, y))
                candidates.extend(get_right_down_candidates(matrix, x, y))
                candidates.extend(get_left_down_candidates(matrix, x, y))
    candidates.sort(key=lambda x: len(x), reverse=True)
    # print(f"{matrix=} {candidates=}")
    return candidates


def s(matrix: list[list[int]]) -> bool:
    """
    1代表空，0代表障碍或者已经被对手连过
    """

    def dfs(matrix: list[list[int]], level) -> bool:
        count = sum([sum(row) for row in matrix])
        print(f"dfs {matrix=}")
        if count == 0:
            return True
        if count == 1:
            return False
        if count == 2:
            return True

        for points in find_all_candidates(matrix):
            print(f"{matrix=} {points=}")
            for p in points:
                matrix[p.y][p.x] = 0

            if dfs(matrix, level + 1) is False:
                ## 恢复 matrix
                for p in points:
                    matrix[p.y][p.x] = 1

                print(f"{matrix=} True")
                if level == 0:
                    print(f"{points=}")
                return True

            ## 恢复 matrix
            for p in points:
                matrix[p.y][p.x] = 1
        print(f"{matrix=} False")
        return False

    ans = dfs(matrix, 0)
    return ans


ans = s([[0, 0, 1, 1], [1, 0, 0, 1], [1, 1, 1, 0], [1, 1, 0, 0]])
# ans = s([[1, 1, 1, 1], [0, 0, 0, 0], [1, 1, 1, 0]])
print(ans)
