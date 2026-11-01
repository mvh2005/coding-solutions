# Maximum Subarray Sum with One Square Allowed

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Given an integer array  **arr[]**, find the maximum subarray sum by squaring at most one element.

 **Examples:** 

```
Input: arr[] =  [-1, -2, 3, -2, 3]
Output: 10
Explanation: The subarray {3, -2, 3} with squaring -2 will give the maximum sum as 3 + 4 + 3 = 10.
```

```
Input: arr[] =  [-4, -4, -2, 5, 2, -1]
Output: 27
Explanation: The subarray {5, 2} with squaring 5 will give a maximum sum of 25 + 2 = 27.
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-11-01T05:40:33.042Z  

```py
class Solution:
    def maximumSubarray(self, arr):
        normal = arr[0]
        squared = arr[0] ** 2

        ans = max(normal, squared)

        for x in arr[1:]:
            new_normal = max(x, normal + x)

            new_squared = max(
                x*x,
                squared + x,
                normal + x*x
            )

            normal = new_normal
            squared = new_squared

            ans = max(ans, normal, squared)

        return ans
```

---

[View on GeeksforGeeks](https://practice.geeksforgeeks.org/problems/maximum-sum-subarray--143510/1)