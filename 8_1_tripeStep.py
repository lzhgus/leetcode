# Triple Step: A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps
# at a time, implement a method to count how many possible ways the child can run up the stairs

#1 Brute force
# What is the very last step that is done?
# the one  that lands A on the nth step was either 3 step , 2 step , or a 1 step hop 

def countWays(n):
    if n < 0: return 0
    elif n == 0: return 1
    else:
        return countWays(n-1) + countWays(n-2) + countWays(n-3)

#2 Brute force + Memoization Solution
# avoid many duplicate values which are unnecessary

def countWays(n):
    memo = [-1]*n
    return countWay(n, memo)

def countWay(n, memo):
    if n < 0 : return 0
    elif n == 0: return 1
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = countWay(n-1, memo) + countWay(n-2, memo) + countWay(n-3, memo)
        return memo[n]


