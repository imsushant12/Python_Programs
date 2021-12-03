"""
Problem Statement:
-----------------
Given an array of strings, group anagrams together.
Example:
Input: [“ate”, ”tan”, “tea”, “eat”, “bat”, “nat”],
Output:
[
[“tea”, ”ate”, “eat”],
["tan","nat"],
["bat"]
]
"""


def string_anargams(words):
    result = []
    groups = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in groups:
            groups[sorted_word].append(word)
        else:
            groups[sorted_word] = [word]

    for key, value in groups.items():
        result.append(value)

    return result


words = ["ate", "tan", "tea", "eat", "bat", "nat"]
answer = string_anargams(words)
print(answer)
