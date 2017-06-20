def flipBit(n):
    m = len('{0:08b}'.format(n)
    if ~n == 0: return len(m)
    sequence = []
    sequence = getAlternatingSequence(n)
    return findLongest(sequence)

def getAlternatingSequence(n, m):
    seq = []
    search = 0
    counter = 0
    for i in range(m):
        if (n&1 != search){
            seq.append(counter)
            search = n & 1
        }
        counter += 1
        n >> 1
    return seq

def findLongest(seq):
    maxseq = 1

    for i in range(0,len(seq),2):
        zeroseq = seq[i]
        right = seq[i-1] if i-1>=0 else 0
        left = seq[i+1] if i+1<len(seq) else 0

        thisseq = 0
        if zeroseq == 1:
            thisseq = right + 1 + left
        elif zeroseq > 1:
            thisseq = 1 + max(right, left)
        elif zeroseq == 0:
            thisseq = max(right, left)

        maxseq = max(thisseq, maxseq)

    return maxseq 

# solution 2 

def flipBit(n):
    m = len('{0:08b}'.format(n))
    if ~n == 0: return m
    
    curLen = 0; preLen = 0; maxLen = 1
    while n != 0:
        if (n&1==1):
            curLen+=1
        elif n&1==0:
            preLen = 0 if n&2==0 else curLen
            curLen = 0
        maxLen = max(preLen+cureLen+1, maxLen)
        n>>1
    return maxLen 
