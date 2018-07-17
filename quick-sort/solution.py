# -*- coding: utf-8 -*-


def quickSort(nums):
    """
    >>> from random import shuffle
    >>> nums = range(10)
    >>> quickSort(nums)
    >>> nums
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> nums = range(10)
    >>> shuffle(nums)
    >>> quickSort(nums)
    >>> nums
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    def quickSort2(nums, low, high):
        # print nums, low, high
        if high - low < 1:
            return

        f = nums[high]
        p = None  # point to first num that's bigger than f
        for i, n in enumerate(nums[low: high]):
            if n >= f:
                if p is None:
                    p = i+low
            else:
                if p is not None:
                    nums[i+low], nums[p] = nums[p], nums[i+low]
                    p += 1

        # print '~~~', nums, p
        if p is not None:
            nums[p], nums[high] = nums[high], nums[p]
            # print '!!!', nums
            quickSort2(nums, low, p-1)
            quickSort2(nums, p+1, high)
        else:
            quickSort2(nums, low, high-1)

    quickSort2(nums, 0, len(nums)-1)


if __name__ == '__main__':
    from random import shuffle
    nums = range(10)
    shuffle(nums)
    # nums = [2, 3, 1]
    print nums
    quickSort(nums)
    print nums
