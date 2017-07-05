# Write a method to return all subsets of a set
#1 Recursion 

def getSubSets(set, index):
    allsubsets = []
    if len(set) == index:
        allsubsets.append([])
    else:
        allsubsets = getSubSets(set, index+1)
        item = set[index]
        moresubsets = []
        for subset in allsubsets:
            newsubset = []
            newsubset.append(subset+[item])
            moresubsets.append(newsubset)
        allsubset.append(moresubsets)
    return allsubsets

#2 dfs
def getSubsets(set):
    res = []
    self.def(set, 0, [], res)
    return res

def dfs(set, index, path, res):
    res.append(path)
    for i in range(index, len(set)):
        dfs(set, index+1, path+[res[i]], res)

#3 
def getSubsets(nums):
    res = [[]]
    for num in nums:
        res += [r + [num] for r in res]
    return res 
