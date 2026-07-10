from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        LOG = 18

        arr = sorted((v, i) for i, v in enumerate(nums))

        values = [x[0] for x in arr]

        pos = [0] * n
        for i, (_, idx) in enumerate(arr):
            pos[idx] = i

        # right reach
        right = [0] * n
        r = 0
        for l in range(n):
            while r + 1 < n and values[r + 1] - values[l] <= maxDiff:
                r += 1
            right[l] = r

        # left reach
        left = [0] * n
        l = 0
        for r in range(n):
            while values[r] - values[l] > maxDiff:
                l += 1
            left[r] = l

        # connected components
        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if values[i] - values[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        upR = [right]
        for _ in range(LOG):
            prev = upR[-1]
            nxt = [0] * n
            for i in range(n):
                nxt[i] = prev[prev[i]]
            upR.append(nxt)

        upL = [left]
        for _ in range(LOG):
            prev = upL[-1]
            nxt = [0] * n
            for i in range(n):
                nxt[i] = prev[prev[i]]
            upL.append(nxt)

        ans = []

        for u, v in queries:
            pu = pos[u]
            pv = pos[v]

            if comp[pu] != comp[pv]:
                ans.append(-1)
                continue

            if pu == pv:
                ans.append(0)
                continue

            if pu < pv:
                cur = pu
                steps = 0
                for k in range(LOG, -1, -1):
                    nxt = upR[k][cur]
                    if nxt < pv:
                        cur = nxt
                        steps += 1 << k
                ans.append(steps + 1)
            else:
                cur = pu
                steps = 0
                for k in range(LOG, -1, -1):
                    nxt = upL[k][cur]
                    if nxt > pv:
                        cur = nxt
                        steps += 1 << k
                ans.append(steps + 1)

        return ans
