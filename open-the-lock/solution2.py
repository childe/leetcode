from collections import deque


class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        initial = "0000"
        if initial in deadends:
            return -1
        status = deque([(initial, 0)])
        visited = set(deadends)
        visited.add(initial)

        while status:
            current_status, step = status.popleft()
            # print current_status, step
            for i in range(0, 4):
                for j in [-1, 1]:
                    # print j
                    next_status = current_status[0:i] + str((int(current_status[i]) - int("0") + j) % 10) + current_status[i+1:]
                    if next_status in visited:
                        continue
                    else:
                        if next_status == target:
                            return step + 1
                        status.append([next_status, step+1])
                        visited.add(next_status)

        return -1


def main():
    import time
    print time.time()
    s = Solution()
    for l in open('testcase.txt'):
        if not l.strip():
            continue
        l = [e.strip() for e in l.strip().split(",")]
        deadends, target = l[:-1], l[-1]
        print s.openLock(deadends, target)
    print time.time()


if __name__ == '__main__':
    main()
