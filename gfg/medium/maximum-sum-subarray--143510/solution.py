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