# num * 2 mean shift left once
def printBinary(num):
    if num >= 1 or num <= 0:
        return "ERROR"

    res = ''
    res += '.'
    while num > 0:
        if len(res) >= 32:
            return "ERROR"
        r = num * 2
        if r >= 1:
            res += '1'
            num = r-1
        else:
            res += '0'
            num = r
    return res

def main():
    a = 0.625
    c = printBinary(a)
    print c

if __name__ == "__main__":
    main()
