"""
Problem Statement:
------------------
Encoding Three Strings: Anand was assigned the task of coming up with an encoding mechanism for any given three strings. He has come up with the below plan

STEP ONE: Given any three strings, break each string into 3
parts each.

For example-If the three strings are as below
Input1= "John" 
Input2= "Johny
Input3= "Janardhan"

"John" should be split into "J", "oh", "n as the FRONT
MIDDLE and END parts respectively.

Johny should be split into "Jo", "h", "ny as the FRONT, MIDDLE and END parts respectively "Janardhan" should be split into "Jan", "and", "han" as the FRONT, MIDDLE and END parts respectively.

If the no. of characters in the string are in multiples of 3 then each split-part will contain equal no of characters as seen in the example of "Janardhan".

If the no. of characters in the string are NOT multiples of 3, and if there is one character more than multiple of 3 then the middle part will get the extra character as seen in the example of "John".

If the no. of characters in the string are NOT in multiples of 3, and if there are two characters more than multiple of 3, then the FRONT and END parts will get one extra character each, as seen in the example of "Johny"

STEP TWO: Concatenate (join) the FRONT, MIDDLE and END parts of the strings as per the below specified concatenation-rule to form three Output strings. 

Output1 = FRONT part of Input1 + MIDDLE part of Input2 +
          END part of Input3 

Output2 = MIDDLE part of Input1 + END part of Input2 +         FRONT part of Input3

Output3 = END part of Input1 + FRONT part of input2 +
          MIDDLE part of Input3

For example, for the above specified example input strings, Output1 = "J" + "h" + "han" = "Jhhan" 
Output2 = "oh" + "ny" "Jan" = "ohnyJan"
Output3 = "n" + "Jo" + "ard" = "nJoard"


STEP THREE: Process the resulting output strings based on the output-processing rule.

After the above two steps, we will now have three output strings. Further processing is required only for the third output string as per below rule - 

"Toggle the case of each character in the string", i.e., in the third output string, all lower-case characters should be made upper-case and vice versa.

For example, for the above example strings, Output3 is
"nJoard", so after applying the toggle rule, Output3 should become "NjOARD"


Final Result - The three output strings after applying the above three steps is the final result. i.e. for the above example,

Output1 = "Jhhan"
Output2 "ohnyJan"
Output3 "NjOARD"
"""


def helperDivisible(s, firsts, mids, lasts, diff):
    end = len(s) - diff
    firsts.append(s[:diff])
    mids.append(s[diff:end])
    lasts.append(s[end:])


def helperNonDivisible(s, firsts, mids, lasts, diff):
    end = len(s) - diff
    firsts.append(s[:diff])
    mids.append(s[diff:end])
    lasts.append(s[end:])


def makeOutputs(firsts, mids, lasts):
    result1 = firsts[0] + mids[1] + lasts[2]
    result2 = mids[0] + lasts[1] + firsts[2]
    result3 = lasts[0] + firsts[1] + mids[2]

    answers = []
    answers.append(result1)
    answers.append(result2)
    answers.append(result3.swapcase())

    return answers


def solve(s, times):
    firsts = []
    mids = []
    lasts = []
    for i in s:
        times = int(times)
        length = len(i)
        if length % times == 0:
            difference = length//times
            helperDivisible(i, firsts, mids, lasts, difference)
        else:
            difference = length % times
            helperNonDivisible(i, firsts, mids, lasts, difference)

    return makeOutputs(firsts, mids, lasts)


s = input().split()
times = input()
print(solve(s, times))
