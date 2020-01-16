# -*- coding: utf-8 -*-

'''
https://leetcode-cn.com/problems/search-insert-position/

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.


Example 1:
Input: [1,3,5,6], 5
Output: 2


Example 2:
Input: [1,3,5,6], 2
Output: 1


Example 3:
Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''


class Solution(object):
    def searchInsert(self, nums, target):
        return (lambda n, t: (lambda f, n, t, s, e, m: f(f, n, t, s, e, m))((lambda f, n, t, s, e, m: s if s > e else m if t == n[m] else f(f, n, t, s, m-1, (s+m-1)//2) if t < n[m] else f(f, n, t, m+1, e, (m+1+e)//2)), n, t, 0, len(n)-1, (len(n)-1)//2))(nums,target)
        return (lambda : lambda n, t: (lambda f, n, t, s, e, m: f(f, n, t, s, e, m))((lambda f, n, t, s, e, m: s if s > e else m if t == n[m] else f(f, n, t, s, m-1, (s+m-1)//2) if t < n[m] else f(f, n, t, m+1, e, (m+1+e)//2)), n, t, 0, len(n)-1, (len(n)-1)//2))()(nums,target)


'''
def searchInsert(nums, target, s, e, m):
    if s > e:
        return s

    if target == nums[m]:
        return m
    if target < nums[m]:
        return searchInsert(nums, target, s, m-1, (s+m-1)//2)
    return searchInsert(nums, target, m+1, e, (m+1+e)//2)
'''


def searchInsert(f, nums, target, s, e, m):
    '''
    if s > e:
        return s

    if target == nums[m]:
        return m
    if target < nums[m]:
        return f(f, nums, target, s, m-1, (s+m-1)//2)
    return f(f, nums, target, m+1, e, (m+1+e)//2)
    '''
    return s if s > e else m if target == nums[m] else f(
        f, nums, target, s, m-1, (s+m-1)//2) if target < nums[m] else f(f, nums, target, m+1, e, (m+1+e)//2)


def r(f, nums, target, s, e, m):
    return f(f, nums, target, s, e, m)


h = lambda n, t: (lambda f, n, t, s, e, m: f(f, n, t, s, e, m))((lambda f, n, t, s, e, m: s if s > e else m if t == n[m] else f(f, n, t, s, m-1, (s+m-1)//2) if t < n[m] else f(f, n, t, m+1, e, (m+1+e)//2)), n, t, 0, len(n)-1, (len(n)-1)//2)



# f = r(searchInsert)


def main():
    s = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    a = 2
    print(searchInsert(searchInsert, nums, target, 0, len(nums)-1, (len(nums)-1)//2))
    print(r(searchInsert, nums, target, 0, len(nums)-1, (len(nums)-1)//2))
    print(h(nums, target))
    assert s.searchInsert(nums, target) == a

    nums = [1, 3, 5, 6]
    target = 2
    a = 1
    print(searchInsert(searchInsert, nums, target, 0, len(nums)-1, (len(nums)-1)//2))
    print(r(searchInsert, nums, target, 0, len(nums)-1, (len(nums)-1)//2))
    print(h(nums, target))
    assert s.searchInsert(nums, target) == a

    nums = [1, 3, 5, 6]
    target = 7
    a = 4
    print(searchInsert(searchInsert, nums, target, 0, len(nums)-1, (len(nums)-1)//2))
    print(r(searchInsert, nums, target, 0, len(nums)-1, (len(nums)-1)//2))
    print(h(nums, target))
    assert s.searchInsert(nums, target) == a

    nums = [1, 3, 5, 6]
    target = 0
    a = 0
    print(searchInsert(searchInsert, nums, target, 0, len(nums)-1, (len(nums)-1)//2))
    print(r(searchInsert, nums, target, 0, len(nums)-1, (len(nums)-1)//2))
    print(h(nums, target))
    assert s.searchInsert(nums, target) == a


if __name__ == '__main__':
    main()
