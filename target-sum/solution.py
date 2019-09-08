class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if sum(nums) < S:
            return 0
        s = sum(nums) - S
        if s % 2 == 1:
            return 0
        P = int(s / 2)
        dp = [1] + [0] * P
        for n in nums:
            for i in range(len(dp)-1, -1, -1):
                if i + n <= P:
                    dp[i+n] += dp[i]

        return dp[P]


def main():
    s = Solution()
    print(s.findTargetSumWays([1, 1], 0))


if __name__ == '__main__':
    main()
