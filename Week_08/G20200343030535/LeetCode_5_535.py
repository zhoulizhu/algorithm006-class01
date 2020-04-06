class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     strlen = len(s)
    #     r = s[::-1]
    #     end = 0
    #     l = 0
    #     dp = [0 for _ in range(strlen + 1)]
    #     for i in range(1,strlen + 1):
    #         for j in range(strlen,0,-1):
    #             if s[i - 1] == r[j - 1]:
    #                 dp[j] = dp[j - 1] + 1
    #             else:
    #                 dp[j] = 0
    #             if dp[j] > l:
    #                 bef = strlen - j
    #                 if bef + dp[j] == i:
    #                     l = dp[j]
    #                     end = i
    #     return s[end - l:end]
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        DP = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            DP[i][i] = True
        for i in range(1, len(s)):
            DP[i][i-1] = True
        longest, start = 1, 0
        for length in range(2, len(s) + 1):
            for i in range(len(s) + 1 - length):
                j = length + i - 1
                if DP[i+1][j-1] and s[i] == s[j]:
                    DP[i][j] = True
                    if length > longest:
                        longest = length
                        start = i
        return s[start : start + longest]

if __name__ == "__main__":
    # palind = Solution().longestPalindrome("aacdefcaa")
    # palind = Solution().longestPalindrome("babad")
    # palind = Solution().longestPalindrome("ccd")
    # palind = Solution().longestPalindrome("cbbd")
    # palind = Solution().longestPalindrome("abcdbbfcba")
    palind = Solution().longestPalindrome("a")
    print(f"longestPalindrome:{palind}")