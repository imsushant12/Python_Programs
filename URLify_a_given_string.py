"""
Problem Statement:
------------------
Write a method to replace all the spaces in a string with ‘%20’. You may assume that the string has sufficient space at the end to hold the additional characters and that you are given the “true” length of the string.
Examples: 

Input: "Mr John Smith", 13
Output: Mr%20John%20Smith

Input: "Mr John Smith   ", 13
Output: Mr%20John%20Smith
"""


def solve_optimized(string):
    string = string.strip()
    i = len(s)

    space_count = string.count(' ')

    # new length that will be formed after replacing space with "%20"
    new_length = i + space_count * 2

    # Start filling character from end
    index = new_length - 1

    string = list(string)

    for f in range(i - 2, new_length - 2):
        string.append('0')

    for j in range(i - 1, 0, -1):
        if string[j] == ' ':
            string[index] = '0'
            string[index - 1] = '2'
            string[index - 2] = '%'
            index = index - 3
        else:
            string[index] = string[j]
            index -= 1

    return ''.join(string)


def solve_extra_space(s, n):
    # removing trailing and starting extra spaces.
    s.strip()
    lst = list(s)

    for i in range(len(lst)):
        if lst[i] == " ":
            lst.pop(i)
            lst.insert(i, "%")
            lst.insert(i+1, "2")
            lst.insert(i+2, "0")

    return "".join(lst)


if __name__ == '__main__':
    s = "Mr John Smith   "
    n = len(s)
    print(solve_extra_space(s, n))
    print(solve_optimized(s))
