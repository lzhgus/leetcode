def getPrev(n):
    tmp = 0; c0 = 0; c1= 0; p = 0
    while tmp & n == 0 and n != 0:
        c0+=1
        tmp >> 1

    while tmp & n == 1:
        c1+=1
        tmp >> 1

    p = c0+c1
    
    if (c0+c1==31 || c0+c1==0):
        return -1

    n |= 1<<p
    n &= ~(1<<p -1)
    n |= (1<<(c1-1))-1

    return n


def getNext(n):
    tmp = 0; c0 = 0; c1 = 0; p = 0
    while tmp & n == 1:
        c1+=1
        tmp >> 1
    
    if tmp == 0: return -1
    while tmp & n == 0 and tmp != 0:
        c0+=1
        tmp >> 1

    p = c0+c1
    n &= (~0 << (p+1))
    
    mask = (1 << (c1+1)) -1 
    n |= mask << (c0-1)

    return n
