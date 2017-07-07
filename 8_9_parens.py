# Impletment an algorithm to print all valid of n pairs of parentheses.

#1 

def generateParens(n):
    dic = set()
    if n == 0: 
        dic.add("")
    else:
        prev = generateParents(n-1)
        for p in prev:
            for i in range(len(p)):
                if p[i] == '(':
                    s = insertInside(p, i)
                    dic.add(s)
            dic.add("()"+p)
    return dic

def insertInside(s, index):
    left = s[:i+1]
    right = s[i:]
    return left+"()"+right 
