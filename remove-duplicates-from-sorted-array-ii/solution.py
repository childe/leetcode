# -*- coding: utf-8 -*-

"""
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/

Given a sorted array nums, remove the duplicates in-place such that duplicates appeared
at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input
array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being
1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being
modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the
input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        i, j, l = 0, 0, len(nums)
        while j < l:
            # print(i,j,l,nums[:l])
            if nums[i] == nums[j]:
                j += 1
                continue
            if j - i <= 2:  ## 不需要移动
                i = j
                j += 1
                continue
            diff = j - i - 2
            for idx in range(j, len(nums)):
                nums[idx - diff] = nums[idx]
            l -= diff
            i += 2
            j = i + 1

        ## 最后还要检查一次
        if j -i <= 2:
            return l
        diff = j - i - 2
        l -= diff
        return l


def main():
    s = Solution()
    nums = [1, 1, 1]
    ans = s.removeDuplicates(nums)
    print(ans)
    print(nums)
    assert ans == 2
    assert nums[:ans] == [1, 1]

    nums = [1, 1, 1, 2, 2, 3]
    ans = s.removeDuplicates(nums)
    print(ans)
    print(nums)
    assert ans == 5
    assert nums[:ans] == [1, 1, 2, 2, 3]

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    ans = s.removeDuplicates(nums)
    assert ans == 7
    assert nums[:ans] == [0, 0, 1, 1, 2, 3, 3]


if __name__ == "__main__":
    main()
