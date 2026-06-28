class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        ans = 1 # first element must be 1

        for i in range(1, len(arr)):
            ans = min(ans + 1, arr[i])

        return ans
