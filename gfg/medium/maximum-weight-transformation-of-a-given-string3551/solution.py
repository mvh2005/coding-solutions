class Solution:
    def getMaxWeight(self, s):
        # code here
        n = len(s)
        dp = [0]*(n+1)      # dp[i] = best score for first i letters
        if n>=1:
            dp[1] = 1
        for i in range(2,n+1):
            # Option 1: letter i stays alone
            alone = dp[i-1] + 1
                    # Option 2: letter i pairs with letter i-1
            if s[i-1]!=s[i-2]:
                pair=4        # different -> 4 points
            else:
                pair=3        # same -> 4 - 1 flip = 3 points
            dp[i] = max(alone,dp[i-2]+pair)

        return dp[n]
        