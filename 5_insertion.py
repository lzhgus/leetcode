def updateBit(n,m,i,j):
    # clear the bits j through i in n
    # shift m so that it lines up with bits j through i
    # merge m and n 

    allOne = ~0
    left = allOne<<(j+1)
    right = (1 << i) - 1
    
    mask = left | right 
    
    cleared = mask & n
    shifted = m << i

    return cleared | shifted 

def main():
    a = 103217; b = 13
    c = updateBit(a,b,4,12)
    print "a: " + '{0:08b}'.format(a) + " b: " + '{0:08b}'.format(b) + " c: " + '{0:08b}'.format(c)
if __name__ == "__main__":
    main()
