class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:

        values = []
        for i in range(len(arr)-k+1):
            rem = arr[:i] + arr[i+k:] 
            
            if rem:
                value = max(rem) - min(rem)
                values.append(value)
            
        return min(values)
            
