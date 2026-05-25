from collections import deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        
        wordSet = set(wordList)

        # If endWord not present
        if endWord not in wordSet:
            return 0

        queue = deque()
        queue.append((beginWord, 1))

        while queue:
            word, steps = queue.popleft()

            # Reached target
            if word == endWord:
                return steps

            # Change one character at a time
            for i in range(len(word)):
                
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    
                    newWord = word[:i] + ch + word[i+1:]

                    if newWord in wordSet:
                        queue.append((newWord, steps + 1))
                        wordSet.remove(newWord)

        return 0
