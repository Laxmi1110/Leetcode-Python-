class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        q = deque([1,2,3,4,5,6,7,8,9])

        while q:
            num = q.popleft()
            if num > high:
                continue
            if num >= low:
                res.append(num)

            last_digit = num % 10
            if last_digit < 9:
                q.append(num * 10 + last_digit + 1)

        return res
