class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        for word in words:
            total = 0
            for ch in word:
                total += weights[ord(ch) - ord('a')]

            val = total % 26
            mapped = chr(ord('z') - val)
            res.append(mapped)

        return ''.join(res)
