"""
Problem Statement:
------------------
Given a string array input1[] and another integer input2[] string encoder function returns a string by following the steps:

Step 1: Consider a word from teh array find the first, middle, and the last character and concatenate them. Let's call this a temp.

Step 2: Now temp string from Step 1 has to be concatenated with itself for input2[] number of times. lets call it as answer.

Step 3: Repeat the above two steps for each word in input1 array and store teh answer in another string array in that order. 

Finally return the string array.
"""

def solve(s, times):
    answerList = []
    for i in s:
        t = times
        first = i[0]
        last = i[len(i) - 1]
        mid = i[len(i)//2]

        currentAnswer = first+mid+last
        answer = currentAnswer

        t = int(times)
        while t > 0:
            answer += currentAnswer
            t -= 1

        answerList.append(answer)
        
    return answerList

s = input().split()
times = input()
print(solve(s, times))
