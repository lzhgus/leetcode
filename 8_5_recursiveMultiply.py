# Write a recursive function to multiply two positive itegers without using the * operator(or / operator).
# You can use addition, substraction, and bit shifting, but you should minimize the number of those operations

#1 eg. 8*7 = 8+8+8+8+8+8+8 like a grid
def minProduct(a,b):
    bigger = a if a>b else b
    smaller = a if a<b else b
    memo = [-1]*smaller
    return minHelper(smaller, bigger)

def minHelper(smaller, bigger, memo):
    if smaller == 0: return 0
    elif smaller == 1: return bigger
    elif memo[smaller] > 0: return memo[smaller]
    
    s = smaller >> 1
    side1 = minHelper(s, bigger, memo)
    side2 = side1 
    if smaller % 2 == 1:
        side2 = minHelper(smaller-s, bigger, memo)

    memo[smaller] = side1 + side2
    return memo[smaller]

#2 
def minProduct(a,b):
    bigger = a if a > b else b
    smaller = a if a < b else a
    return helper(smaller, bigger)

def helper(smaller, bigger):
    if smaller == 0: return 0
    elif smaller == 1: return bigger

    s = smaller >> 1
    halfProd = helper(s, bigger)

    if smaller % 2 == 0:
        return halfProd + halfProd
    else:
        return halfProd + halfProd + bigger 

