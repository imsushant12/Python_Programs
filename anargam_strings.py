""""
Probem Statement:
----------------
Given two strings s and t , write a function to determine if t is an anagram of s.
Input: s = "anagram", t = "nagaram"
Output: true
Input: s = "rat", t = "car"
Output: false
You may assume the string contains only lowercase alphabets.
What if the inputs contain unicode characters? How would you adapt your solution to such
case?
"""

def anargams(s, t):
    new_s = ''.join(sorted(s))
    new_t = ''.join(sorted(t))

    if new_s == new_t:
        return True
    else:
        return False


if __name__ == "__main__":
    s = "rat"
    t = "car"
    print(anargams(s, t))