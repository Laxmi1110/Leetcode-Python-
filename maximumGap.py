class Solution:
    def maximumGap(self, nums):
        n = len(nums)

        # If less than 2 elements
        if n < 2:
            return 0

        min_num = min(nums)
        max_num = max(nums)

        # If all numbers are same
        if min_num == max_num:
            return 0

        # Bucket size and count
        bucket_size = max(1, (max_num - min_num) // (n - 1))
        bucket_count = ((max_num - min_num) // bucket_size) + 1

        # Initialize buckets
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]

        # Put numbers into buckets
        for num in nums:
            idx = (num - min_num) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)

        # Find maximum gap
        max_gap = 0
        prev_max = min_num

        for bucket in buckets:
            # Skip empty buckets
            if bucket[0] == float('inf'):
                continue

            # Gap between buckets
            max_gap = max(max_gap, bucket[0] - prev_max)

            prev_max = bucket[1]

        return max_gap
