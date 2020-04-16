# -*- coding: utf-8 -*-

'''
https://leetcode-cn.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

'''


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        mid_point = set()
        res=[]
        point=set()#存所有的单点
        for i in intervals:
            if i[0]==i[1]:point.add(i[0])
            else:
                for j in range(i[0],i[1]):
                    mid_point.add(j+0.5)
        mid_point=sorted(list(mid_point))
        point=sorted(list(point))
        #一个点代表一个长度为1的线段
        if mid_point:
            while len(point)!=0:
                if point[0]<int(mid_point[0]-0.5):
                    res.append([point[0],point[0]])
                    del point[0]
                else:break
        else:
            while len(point)!=0:
                res.append([point[0],point[0]])
                del point[0]
            return res
        for i in mid_point:
            if len(res)==0 or res[-1][1]+0.5!=i: res.append([int(i-0.5),int(i+0.5)])
            else: res[-1][1]=int(i+0.5)
            while len(point)!=0:

                if point[0]>res[-1][1]:break
                elif point[0]>=res[-1][0] and point[0]<=res[-1][1]:del point[0]
                else:
                    temp=res[-1]
                    del res[-1]
                    res.append([point[0],point[0]])
                    res.append(temp)
                    del point[0]
        while len(point)!=0:
            if point[0]>=res[-1][0] and point[0]<=res[-1][1]:del point[0]
            else:
                res.append([point[0],point[0]])
                del point[0]
        return res


def main():
    s = Solution()
    r = s.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    a = [[1, 6], [8, 10], [15, 18]]
    assert r == a

    r = s.merge([[1, 4], [4, 5]])
    a = [[1, 5]]
    assert r == a

    r = s.merge([[1, 4], [0, 4]])
    a = [[0, 4]]
    assert r == a

    r = s.merge([[1, 4], [2, 3]])
    a = [[1, 4]]
    assert r == a


if __name__ == '__main__':
    main()
