# Permutaions without Dups: write a method to compute all permuations of a string of unique characters

#1 recursive build from permutations of first n-1 charators

def getPerms(str):
    if not str: return None
    
    res = []
    if len(str) == 0: 
        res.append("")
        return res

    first = str[0]
    remains = str[1:]
    words = getPerms(remains)
    for word in words:
        for i in range(len(word)):
            s = insertAt(word, first, i)
            res.append(s)
    return res 

def insertAt(word, first, index):
    start = word[:index]
    end = word[index:]
    return start+first+end


#2 build from permutations of all n-1 charators

def getPerms(remainder):
    size = len(remainder)
    res = []
    if size == 0: 
        res.append("")
        return res 
    
    for i in range(size):
        before = remainder[:i]
        after = remainder[i+1:]
        partials = getPerms(before+after)
        
        for s in partials:
            res.append(remainder[i]+s)
    return res 

#3 with duplicate

def printPerms(s):
    res = []
    dic = {}
    for c in s:
        dic[c] = dic.get(c, 0)+1
    
    getPerms(dic, "", len(s), res)

    return res

def getPerms(dic, prefix, remains, res):
    if remains == 0: 
        res.append(prefix)
        return 
    for c in dic.keys():
        count = dic[c]
        if count > 0:
            dic[c] = count-1
            getPerms(dic, prefix+c, remains-1, res)
            dic[c] = count 
    
