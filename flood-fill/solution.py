# -*- coding: utf-8 -*-

'''
https://leetcode-cn.com/problems/flood-fill/

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

'''


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        visited = set()
        color = image[sr][sc]

        def dfs(sr, sc):
            if image[sr][sc] != color:
                return
            if (sr, sc) in visited:
                return
            visited.add((sr, sc))

            image[sr][sc] = newColor
            if sr-1 >= 0:
                dfs(sr-1, sc)
            if sr+1 < len(image):
                dfs(sr+1, sc)
            if sc-1 >= 0:
                dfs(sr, sc-1)
            if sc+1 < len(image[sr]):
                dfs(sr, sc+1)

        dfs(sr, sc)
        return image


def main():
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr, sc, newColor = 1, 1, 2
    output = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]

    s = Solution()
    a = s.floodFill(image, sr, sc, newColor)
    print(a)
    print(a == output)


if __name__ == '__main__':
    main()
