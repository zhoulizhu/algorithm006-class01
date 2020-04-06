import sys
class Solution:
    # def lengthOfLIS(self, nums: list) -> int:
    #     nlen = len(nums)
    #     if nlen == 1:return 1
    #     maxLength = 0
    #     for i in range(1,nlen + 1):
    #         dp = [0  for _ in range(nlen + 1)]
    #         maxi = -sys.maxsize
    #         last = maxi
    #         for j in range(i,nlen + 1):
    #             if nums[j - 1] > maxi:
    #                 dp[j] = dp[j - 1] +1
    #                 last = maxi
    #                 maxi = nums[j - 1]
    #             else:
    #                 dp[j] = dp[j - 1]
    #                 if nums[j - 1] > last:
    #                     maxi = min(maxi,nums[j - 1])
    #         maxLength = max(dp[nlen],maxLength)
    #     return maxLength
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]: 
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

if __name__ == "__main__":
    # l = Solution().lengthOfLIS([1,10,9,2,5])
    # l = Solution().lengthOfLIS([10,9,2,5,3,7,101,18])
    # l = Solution().lengthOfLIS([2,3,1,10,9,2,5,3,7])
    l = Solution().lengthOfLIS([2,3,1,10,9,2,5,3,7,101,18,3,111])
    # l = Solution().lengthOfLIS([-2,-1])
    # l = Solution().lengthOfLIS([10,9,2,5,3,4])
    print(f"l:{l}")
