"""
Problem Statement:
------------------
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.
Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Example 1:
Input: s = "abbaca"
Output: "ca"
Explanation: For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move. The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

Example 2:
Input: s = "azxxzy"
Output: "ay" 

Constraints:
1 <= s.length <= 10^5
s consists of lowercase English letters.
"""


def solve(s):
    stack = []
    i = 0
    while i < len(s):
        if (len(stack) > 0) and (s[i] == stack[len(stack) - 1]):
            stack.pop()
        else:
            stack.append(s[i])
        i += 1

    return "".join(stack)


if __name__ == '__main__':
    s = "abbaca"

    print(solve(s))
