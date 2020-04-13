from collections import defaultdict


def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList or not endWord or not beginWord or not wordList:
        return 0
    L = len(beginWord)
    # 字典，用来保存可以形成的单词的组合，
    # 从任何给定的词。一次换一个字母。
    all_combo_dict = defaultdict(list)
    for word in wordList:
        for i in range(L):
            # Key为通用词
            # Value为具有相同中间属词的单词列表。
            all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)
    # Queue for BFS
    queue = [(beginWord, 1)]
    # 确保我们不会重复处理相同的单词。
    visited = {beginWord: True}
    while queue:
        current_word, level = queue.pop(0)
        for i in range(L):
            # 当前单词的中间词
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]
            # 下一个状态是所有处于相同中间状态的单词。
            for word in all_combo_dict[intermediate_word]:
                # 如果我们找到了我们要找的东西，即结束词-我们可以返回答案。
                if word == endWord:
                    return level + 1
                # 否则，将其添加到BFS队列。也标志它已被访问
                if word not in visited:
                    visited[word] = True
                    queue.append((word, level + 1))
            all_combo_dict[intermediate_word] = []
    return 0


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    ret = ladderLength(beginWord, endWord, wordList)
    print(ret)
