'''
Problem Statement:
-----------------
You are given a string s containing lowercase English letters, and a matrix shift in 3-d array, where shift[i] = [direction, amount]:
direction can be 0 (for left shift) or 1 (for right shift).
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning. Return the final string after all operations.

Example 1:
Input: s = "abc", shift = [[0,1],[1,2]]
Output: "cab"
Explanation:
[0,1] means shift to left by 1. "abc" -> "bca"
[1,2] means shift to right by 2. "bca" -> "cab"
'''

def shift_string(s, shifts):
    answer_string = ""
    final_shift = 0
    string_length = len(s)
    for i in range(len(shifts)):
        direction = shifts[i][0]
        current_shift = shifts[i][1]

        if direction == 0:
            final_shift -= current_shift
        else:
            final_shift += current_shift

    # Calculating the overall shifts needed.
    final_shift %= string_length

    # Performing the shift
    if final_shift > 0:
        answer_string = s[string_length - final_shift:] + s[0:string_length - final_shift]
    else:
        final_shift = abs(final_shift)
        answer_string = s[final_shift:] + s[0:final_shift]

    print(answer_string)


if __name__ == "__main__":
    s = "abc"
    shifts = [[0, 1], [1, 2]]
    shift_string(s, shifts)
