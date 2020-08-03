from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if not wordList or endWord not in wordList:
            return 0

        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + '*' + word[i + 1:]].append(word)

        queue = [(beginWord, 1)]
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.pop(0)
            for i in range(L):
                temp_word = current_word[:i] + '*' + current_word[i + 1:]
                for word in all_combo_dict[temp_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[temp_word] = []
        return 0
sol = Solution()
ret = sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
print(ret)