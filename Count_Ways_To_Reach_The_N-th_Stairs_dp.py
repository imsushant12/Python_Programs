"""
Problem Statement:
------------------
You have been given a number of stairs. Initially, you are at the 0th stair, and you need to reach the Nth stair. Each time you can either climb one step or two steps. You are supposed to return the number of distinct ways in which you can climb from the 0th step to Nth step.

Example :
N=3
We can climb one step at a time i.e. {(0, 1) ,(1, 2),(2,3)} or we can climb the first two-step and then one step i.e. {(0,2),(1, 3)} or we can climb first one step and then two step i.e. {(0,1), (1,3)}.

Input format :
The first line contains an integer 'T', which denotes the number of test cases or queries to be run. Then the test cases follow.
The first and the only argument of each test case contains an integer 'N', representing the number of stairs.

Output Format :
For each test case/query, print the number of distinct ways to reach the top of stairs. Since the number can be huge, so return output modulo 10^9+7.

Constraints :
1 <= 'T' <= 10
0 <= 'N' <= 10^5

Where 'T' is the number of test cases, and 'N' is the number of stairs.

It is guaranteed that sum of 'N' over all test cases is <= 10^5.
Sample Input 1 :
2
2
3
Sample Output 1 :
2
3
Explanation Of Sample Input 1 :
In the first test case, there are only two ways to climb the stairs, i.e. {1,1} and {2}.

In the second test case, there are three ways to climb the stairs i.e. {1,1,1} , {1,2} and {2,1}.
Sample Input 2 :
2
4
5
Sample Output 2 :
5
8
Explanation Of Sample Input 2 :
In the first test case, there are five ways to climb the stairs i.e. {1,1,1,1} , {1,1,2} , {2,1,1} , {1,2,1} , {2,2}.

In the second test case, there are eight ways to climb the stairs i.e. {1,1,1,1,1} , {1,1,1,2} , {1,1,2,1}, {1,2,1,1}, {2,1,1},{2,2,1},{2,1,2} and {2,2,1}.
"""


# Time Complexity : O(n)
# Space Complexity : O(n) + O(n) == O(n)
def recursiveSolution(n):
    if n == 0:
        return 1
    if n < 0:
        return 0

    oneStep = recursiveSolution(n-1)
    twoSteps = recursiveSolution(n-2)

    return oneStep + twoSteps


def dpMemorizationSolution(n, dp):
    if n <= 2:
        return n

    if dp[n] != -1:
        return dp[n]

    dp[n] = dpMemorizationSolution(n-1, dp) + dpMemorizationSolution(n-2, dp)
    return dp[n]


# Time Complexity : O(n)
# Space Complexity : O(n)
def dpTabulationSolution(n):
    dp = []
    dp.append(0)        # dp[0] = 0
    dp.append(1)        # dp[1] = 1
    dp.append(2)        # dp[2] = 2

    for i in range(2, n+1):
        currentWays = dp[i-1] + dp[i-2]
        dp.append(currentWays)

    return dp[n]


# Time Complexity : O(n)
# Space Complexity : O(1)
def spaceOptimizedSolution(n):
    if n <= 2:
        return n

    # initially adding the base values.
    first = 1
    second = 2

    currentWays = 0
    for i in range(3, n+1):
        currentWays = first + second
        first = second
        second = currentWays

    return currentWays


if __name__ == "__main__":
    n = 5
    dp = [-1] * (n+1)
    print(f"Number of ways to reach {n}th stair are:",
          spaceOptimizedSolution(n))
