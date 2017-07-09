# Given an infinite number of quarters, dimes, nickels, and pennies, write code to calculate the number of ways of representing n cents
def change(n):
    denoms = [25, 10, 5, 1]
    dic = [[0 for x in range(n+1)] for y in range(len(denoms))]
    return makeChange(n, denoms, 0)

def makeChange(amount, denoms, index, dic):
    if dic[amount][index] > 0:
        return dic[amount][index]
    
    if index >= len(denoms)-1: return 1
    ways = 0
    denomAmount = denoms[index]
    for i in range(0, amount+1, denomAmount):
        remains = amount - i*denomAmount
        ways += makeChange(remains, denoms, index+1, dic)
    dic[amout][index] = ways
    return ways 

# makeChange(100) = makeChange(100 using 0 quarters) + makeChange(100 using 1 quarters) + makeChange(100 using 2 quarters) + makeChange(100 using 3 quarters) + makeChange(100 using 4 quarters)
#                 = makeChange(100 using 0 quarters) + makeChange(75 using 0 quarters) + makeChange(50 using 0 quarters) + makeChange(25 using 0 quarters) + 1

# makeChange(100 using 0 quarters) = makeChange(100 using 0 quarters, 0 dimes) + makeChange(100 using 0 quarters, 1 dimes) + makeChange(100 using 0 quarters, 2 dimes) + ... +
                                     makeChange(100 using 0 quarters, 10 dimes)
