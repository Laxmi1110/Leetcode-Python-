from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def dfs(start: int) -> List[str]:
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""] # base: one valid decomposition of empty string

            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    sub_sentences = dfs(end)
                    for sub in sub_sentences:
                        if sub: # avoid trailing space
                            res.append(word + " " + sub)
                        else:
                            res.append(word)

            memo[start] = res
            return res

        return dfs(0)
