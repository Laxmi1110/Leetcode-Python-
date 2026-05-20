from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        wordSet = set(wordList)
        
        if endWord not in wordSet:
            return []
        
        # Store parents of each word
        parents = defaultdict(list)
        
        # BFS
        level = {beginWord}
        found = False
        
        while level and not found:
            
            next_level = defaultdict(list)
            
            # Remove visited words from wordSet
            for word in level:
                if word in wordSet:
                    wordSet.remove(word)
            
            for word in level:
                
                for i in range(len(word)):
                    
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        
                        newWord = word[:i] + ch + word[i+1:]
                        
                        if newWord in wordSet:
                            next_level[newWord].append(word)
                            
                            if newWord == endWord:
                                found = True
            
            # Save parents
            for word, par in next_level.items():
                parents[word].extend(par)
            
            level = next_level.keys()
        
        # Backtracking to build paths
        res = []
        
        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            
            for par in parents[word]:
                dfs(par, path + [par])
        
        if found:
            dfs(endWord, [endWord])
        
        return res
